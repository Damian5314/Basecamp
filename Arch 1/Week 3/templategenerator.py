import re
import datetime

while True:
    more_letters = input("More Letters?(Yes or No): ")
    if more_letters == "No":
        break
    elif more_letters == "Yes":
        offer_rejection = input("Job Offer or Rejection?: ")
        if offer_rejection == "Job Offer":
            while True:
                first_name = input("First Name?: ").capitalize()
                if 2 <= len(first_name) <= 10 and not re.search(r'\d', first_name):
                    break
                else:
                    print("Input error")
            while True:
                last_name = input("Last name?: ").capitalize()
                if 2 <= len(last_name) <= 10 and not re.search(r'\d', last_name):
                    break
                else:
                    print("Input error")
            while True:
                job_title = input("Job Title?: ")
                if len(job_title) >= 10 and not re.search(r'\d', job_title):
                    break
                else:
                    print("Input error")
            while True:
                try:
                    annual_salary_str = input("Annual Salary?(between 20.000,00 and 80.000,00): ")
                    annual_salary_str2 = annual_salary_str.replace('.', '').replace(',', '')
                    annual_salary = int(annual_salary_str2)
                    if 2000000 <= annual_salary <= 8000000:
                        break
                    else:
                        print("Input error")
                except ValueError:
                    print = ("Input error")
            while True:
                start_date = input("Start Date? (YYYY-MM-DD): ")
                try:
                    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                    if start_date.year in (2021, 2022):
                        real_start_date = start_date.strftime('%Y-%m-%d')
                        print(real_start_date)
                        break
                    else:
                        print("Input error")
                except ValueError:
                    print("Input error")
            job_offer = f"""
Here is the final letter to send:
Dear {first_name} {last_name},
After careful evaluation of your application for the position of {job_title},
we are glad to offer you the job. Your salary will be {annual_salary_str} euro annually.
Your start date will be on {real_start_date}. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
            """
            print(job_offer)
        elif offer_rejection == "Rejection":
            while True:
                first_name = input("First Name?: ").capitalize()
                if 2 <= len(first_name) <= 10 and not re.search(r'\d', first_name):
                    break
                else:
                    print("Input error")
            while True:
                last_name = input("Last name?: ").capitalize()
                if 2 <= len(last_name) <= 10 and not re.search(r'\d', last_name):
                    break
                else:
                    print("Input error")
            while True:
                job_title = input("Job Title?: ")

                if len(job_title) >= 10 and not re.search(r'\d', job_title):
                    break
                else:
                    print("Input error")
            feedback = input("Feedback? (Yes or No): ")
            feedback_statement = ""
            while True:
                if feedback == "Yes":
                    text_feedback = input("Enter your Feedback (One Statement): ").capitalize()
                    rejectionF_letter = f"""
Here is the final letter to send:
Dear {first_name} {last_name},
After careful evaluation of your application for the position of {job_title},
at this moment we have decided to proceed with another candidate.
Here we would like to provide you our feedback about the interview.
{text_feedback}
We wish you the best in finding your future desired career.
Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
                    """
                    print(rejectionF_letter)
                    break
                elif feedback == "No":
                    Rejection_Letter = f"""
Here is the final letter to send:
Dear {first_name} {last_name},
After careful evaluation of your application for the position of {job_title},
at this moment we have decided to proceed with another candidate.
We wish you the best in finding your future desired career.
Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
                    """
                    print(Rejection_Letter)
                    break
    else:
        print("Input error")