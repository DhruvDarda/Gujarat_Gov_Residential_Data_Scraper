import scrapy
import json

class ProjectSpider(scrapy.Spider):
    name = "project_spider"
    start_urls = [
        "https://gujrera.gujarat.gov.in/dashboard/get-district-wise-projectlist/0/0/all/Gandhinagar/all"
    ]

    def parse(self, response):
        # Parse the JSON response
        try:
            data = json.loads(response.text)
            if data.get("status") == "200" and data.get("data"):
                for project in data["data"]:
                    yield {
                        "projectRegId": project.get("projectRegId"),
                        "districtType": project.get("districtType"),
                        "disposed_date": project.get("disposed_date"),
                        "project_ack_no": project.get("project_ack_no"),
                        "promoterName": project.get("promoterName"),
                        "districtName": project.get("districtName"),
                        "total_est_cost_of_proj": project.get("total_est_cost_of_proj"),
                        "projectCost": project.get("projectCost"),
                        "projectType": project.get("projectType"),
                        "approvedOn": project.get("approvedOn"),
                        "endDate": project.get("endDate"),
                        "hardcopysubmissionDate": project.get("hardcopysubmissionDate"),
                        "payment_status": project.get("payment_status"),
                        "payment_token": project.get("payment_token"),
                        "pmtr_email_id": project.get("pmtr_email_id"),
                        "pr_mobile_no": project.get("pr_mobile_no"),
                        "prmtr_adhaar_no": project.get("prmtr_adhaar_no"),
                        "prmtr_com_reg_no": project.get("prmtr_com_reg_no"),
                        "prmtr_pan_no": project.get("prmtr_pan_no"),
                        "project_address": project.get("project_address"),
                        "project_cost": project.get("project_cost"),
                        "project_status": project.get("project_status"),
                        "startDate": project.get("startDate"),
                        "projectName": project.get("projectName"),
                        "wfoid": project.get("wfoid"),
                        "promoterAddress": project.get("promoterAddress"),
                        "regFee": project.get("regFee"),
                        "projOrgFDate": project.get("projOrgFDate"),
                        "extDate": project.get("extDate"),
                        "regNo": project.get("regNo"),
                    }
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON: {e}")

