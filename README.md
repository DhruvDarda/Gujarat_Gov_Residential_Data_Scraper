
# Gujarat_Gov_Residential_Data_Scraper

This project is a scraper designed to collect residential project data from the Gujarat government's online portal. The scraper extracts details about various residential projects including project registration IDs, cost, promoter details, and much more. The scraped data is saved in CSV format for easy access and analysis.

## Requirements

To run this scraper, you need to have Python and Scrapy installed. If you don't have Scrapy installed, follow the steps below to set up the environment.

### Installation

1. **Install Python**  
   If you don't have Python installed, download and install it from [here](https://www.python.org/downloads/).

2. **Install Scrapy**  
   You can install Scrapy using pip. Run the following command in your terminal or command prompt:

   ```bash
   pip install scrapy
   ```

3. **Clone the repository**

   If you haven't already, clone the project to your local machine:

   ```bash
   git clone https://github.com/yourusername/Gujarat_Gov_Residential_Data_Scraper.git
   ```

4. **Navigate to the project directory**

   ```bash
   cd Gujarat_Gov_Residential_Data_Scraper
   ```

## Running the Spider

To run the spider and start scraping the data, use the following command:

```bash
scrapy crawl project_spider -o file_name.csv
```

This will start the scraper and save the scraped data into a CSV file named `file_name.csv`.

### Output

The data will include the following fields:

- `projectRegId`
- `districtType`
- `disposed_date`
- `project_ack_no`
- `promoterName`
- `districtName`
- `total_est_cost_of_proj`
- `projectCost`
- `projectType`
- `approvedOn`
- `endDate`
- `hardcopysubmissionDate`
- `payment_status`
- `payment_token`
- `pmtr_email_id`
- `pr_mobile_no`
- `prmtr_adhaar_no`
- `prmtr_com_reg_no`
- `prmtr_pan_no`
- `project_address`
- `project_cost`
- `project_status`
- `startDate`
- `projectName`
- `wfoid`
- `promoterAddress`
- `regFee`
- `projOrgFDate`
- `extDate`
- `regNo`


