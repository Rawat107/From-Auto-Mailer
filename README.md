# Google Form Submission Automation

This project automates the submission of a Google form and sends a confirmation email with a screenshot of the submission confirmation page. It uses Selenium to fill out the form and Django to send the email. The system runs in a console-based environment where user inputs are taken from the console.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your version of Google Chrome)

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/google-form-submission-automation.git
   cd google-form-submission-automation
   ```

2. **Install the Required Packages:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Email Settings:**

   Open `form_submitter/settings.py` and update the email configuration with your email details:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-email-password'
   ```

## Usage

1. **Open a New Terminal and Run the Form Submission Script:**

   ```sh
   python manage.py submit_and_email
   ```

2. **Enter the Required Details in the Console:**

   When prompted, enter the required details such as:
   - Full Name
   - Contact Number
   - Email ID
   - Full Address
   - Pin Code
   - Date of Birth
   - Gender
   - Verification Code

The script will fill out the form, submit it, take a screenshot of the confirmation page, and send an email with the screenshot attached.

##License

This project is licensed under the MIT License.
