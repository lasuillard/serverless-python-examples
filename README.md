# serverless-python-examples

Examples deploying Python applications using serverless framework.

## Quick Start

Clone the repository:

```bash
$ git clone https://github.com/lasuillard/serverless-python-examples
```

Install the project deps (npm) for [serverless](https://www.serverless.com/) CLI and plugins:

```bash
$ npm install
$ alias sls="npx serverless" # For convenience
```

Create an access key for your IAM. I recommend creating an IAM and giving appropriate permissions. I gave following (just for convenience, **not recommended for production**) permissions to new IAM account:

- AmazonEC2ContainerRegistryFullAccess
- AmazonS3FullAccess
- AWSCloudFormationFullAccess
- AWSLambda_FullAccess
- CloudWatchLogsFullAccess
- IAMFullAccess

Then configure the profile **serverless-python-examples**. Region is not necessarily to be **us-east-1**, choose what you want.

```bash
$ aws configure --profile serverless-python-examples
AWS Access Key ID [None]: XXXXXXXXXXXXXXXXXXXX
AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Default region name [None]: us-east-1
Default output format [None]:
```

Move to the app and deploy:

```bash
$ cd fastapi-playwright
$ sls deploy
(node:400182) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)

Deploying serverless-python-examples to stage dev (us-east-1)
Updated AWS resource tags..
Updated AWS resource tags..
Updated APIGateway resource tags..

✔ Service deployed to stack serverless-python-examples-dev (289s)

endpoint: https://35fg4ihpurh2jfkoo6luv74etu0drsry.lambda-url.us-east-1.on.aws/
functions:
  app: serverless-python-examples-dev-app

Need a faster logging experience than CloudWatch? Try our Dev Mode in Console: run "serverless dev"
```

serverless will take care of creating all necessary resources: S3 bucket, ECR repository and Lambda functions, CloudWatch log groups.

Copy the endpoint URL (https://35fg4ihpurh2jfkoo6luv74etu0drsry.lambda-url.us-east-1.on.aws/ above) for later testing.

## Testing

Once deployed, CLI will show the URL of Lambda endpoint. Access the root URL with query parameter `url`, for example:

```bash
$ curl https://35fg4ihpurh2jfkoo6luv74etu0drsry.lambda-url.us-east-1.on.aws/?url=https://example.com
"Example Domain"
```

Function will respond with given URL's page title.

To see logs, run:

```bash
$ sls logs --function app --tail
```

## Cleanup Resources

Remove resources created by serverless:

```bash
$ sls remove
```

It will remove all the resources created by CLI.

As AWS CLI does not provide removing profile you should edit **~/.aws/credentials** file and remove the **serverless-python-examples** profile manually.

Delete the IAM if you created one, and no need anymore.

## References

- https://www.cloudtechsimplified.com/playwright-aws-lambda-python/
- https://github.com/umihico/docker-selenium-lambda
