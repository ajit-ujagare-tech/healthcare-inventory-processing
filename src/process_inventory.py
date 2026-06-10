import pandas as pd
import logging
import configparser

# Read configuration
config = configparser.ConfigParser()
config.read("config/config.ini")

input_file = config["PATHS"]["INPUT_FILE"]
output_file = config["PATHS"]["OUTPUT_FILE"]
log_file = config["PATHS"]["LOG_FILE"]

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Inventory Processing Started")

    # Read file
    df = pd.read_csv(input_file)

    logging.info(f"Records Read: {len(df)}")

    # Remove duplicate accounts
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    logging.info(f"Duplicates Removed: {before - after}")

    # Remove non-dialable accounts
    excluded_status = ["BANKRUPT", "DISPUTE"]

    df = df[~df["status"].isin(excluded_status)]

    logging.info(f"Eligible Accounts: {len(df)}")

    # Find missing phone numbers
    missing_phone = df["phone"].isna().sum()

    logging.info(f"Missing Phones: {missing_phone}")

    # Save output
    df.to_csv(output_file, index=False)

    logging.info("Output File Generated Successfully")

    print("Processing Completed Successfully")

except Exception as e:
    logging.error(str(e))
    print("Processing Failed")
