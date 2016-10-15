# Lambda Starter Kit (lambdaStarter)

lambdaStarter is a lightweight framework designed to help start new Python based Lambda projects. The starter kit encourages the use of Emulambda, a utility which helps speed up development of Lambda functions by emulating Lambda on your local environment. The starter kit also makes use of the lambda-uploader utility which helps deliver the Lambda function in a consistent way to AWS Lambda.

# Maintainer
Kevin Epstein (kevin@epstein.co.za)

## Requirements
Requirements (non-standard Python libraries that your Lambda function will need) should be stored in the [requirements.txt](requirements.txt) file. Packages can also be installed in "editable" form. Editable notation for the requirements.txt file can be found at https://pip.readthedocs.io/en/1.1/requirements.html#the-requirements-file-format

| Package Name | Version | URL (Optional) |
|---------------|----------------|---------------|
| Emulambda | 0.1 | https://github.com/fugue/emulambda |
| lambda-uploader | 1.0.3 | https://github.com/rackerlabs/lambda-uploader |

# Preparing your environment
1. Create a new project directory `mkdir my_new_project`
2. Change to the project directory `cd my_new_project`
3. Clone this repo into your project directory `git clone https://github.com/kepstein/lambdaStarter .`
4. Start a new virtual environment `virtualenv my_new_project`
5. Install Emulambda `pip install git+https://github.com/fugue/emulambda.git`
6. Install lambda-uploader `pip install lambda-uploader`
7. Configure the lambda-uploader configuration file ([lambda.json](lambda.json))

# Proposed development workflow
I developed this workflow while building a Lambda function as the engine to an Amazon Alexa Skill. If you already have a workflow that works well for you, you probably do not need to follow this proposed workflow. If however you're new to Lambda functions development, you might find this workflow helpful.

1. Create simple tests in the test.py file
2. Perform unit test your code with something like nose2 (define your tests in test.py in the tests directory)
3. Perform system tests using emulambda. Emulambda expects an event to be passed to the Lambda function. I've included a sample event (s3put.json) in the events directory. If you want to test with actual events, you'll have to capture the event using a simple Lambda function and then save the event as a json file in your events directory.
4. When you're satusfied that both your unit and system tests are passing, build and deploy your Lambda function using lambda-builder
5. Repeat

## IAM Role Capability requirements
* Basic Lambda execution