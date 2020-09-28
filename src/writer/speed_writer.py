from .writer import Writer
import datetime
import random
import json
import logging
import subprocess

class SpeedWriter(Writer):
    SPEEDTEST_TIMEOUT_SECONDS = 180

    def get_data(self):
        logging.info("Getting data")
        return self._run_speedtest()

    def write_data(self):
        return_data = self.get_data()
        self.influx_client.write_points(
            self._get_down_datapoint(return_data["download"]), 
            database=self.db_name, 
            time_precision='ms', 
            batch_size=10000
        )
        self.influx_client.write_points(
            self._get_up_datapoint(return_data["upload"]), 
            database=self.db_name, 
            time_precision='ms', 
            batch_size=10000
        )

    def _run_speedtest(self):
        return_data = {
            "download": 0,
            "upload": 0
        }
        logging.info("Starting speedtest process")
        process = subprocess.Popen(
            [
                "speedtest", 
                "-p", "no",
                "--format", "json",
                "--accept-license",
            ],
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            universal_newlines=True)
        try:
            stdout, stderr = process.communicate(timeout=self.SPEEDTEST_TIMEOUT_SECONDS)
            if process.returncode == 0:
                logging.info("Speedtest process finished successfully")
                download, upload = self._convert_speedtest_out_json_to_datapoint(json.loads(stdout))
                return_data["download"] = download
                return_data["upload"] = upload
            else:
                logging.error("Speedtest command exited with non-zero exit code.\nStderr: {stderr}\nStdout: {stdout}")
        except subprocess.TimeoutExpired as e:
            logging.error("Speedtest command timed out, consider increasing the timeout limit")
            process.kill()
        except Exception as e:
            logging.error("Speedtest command failed, no datapoint can be captured")
            process.kill()
        return return_data
        
    def _convert_speedtest_out_json_to_datapoint(self, speedtest_data):
        return speedtest_data["download"]["bytes"], speedtest_data["upload"]["bytes"]

    def _get_down_datapoint(self, download_speed):
        datapoint = {
            "measurement": "internet_speed_down",
            "tags": {
                "type": "speed",
            },
            "time": datetime.datetime.now(),
            "fields": {
                "value": download_speed
            }
        }
        logging.info(f"Download speed: {download_speed}")
        return [datapoint]

    def _get_up_datapoint(self, upload_speed):
        datapoint = {
            "measurement": "internet_speed_up",
            "tags": {
                "type": "speed",
            },
            "time": datetime.datetime.now(),
            "fields": {
                "value": upload_speed
            }
        }
        logging.info(f"Upload speed: {upload_speed}")
        return [datapoint]
