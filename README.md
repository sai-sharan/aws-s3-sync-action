# AWS S3 Sync GitHub Action

`aws-s3-sync-action` is a GitHub action, which allows you to sync data from your GitHub repo or data created in your workflows to a S3 bucket that you have access to.

### How to use `aws-s3-sync-action` ?

When configuring your workflow, you can reference this action in your workflow file to sync data from your GitHub repo or data created in your workflows to a S3 bucket that you have access to.


Example:

Say you have built or are building a React App and are using AWS S3 to host the app for static web hosting.

After working on the app locally, you are pushing your code to GitHub and you want to automate the process of building your app, testing it and pushing the build to S3.

Below is a sample workflow to help you achieve this with `aws-s3-sync-action`:

```yaml
name: Build and Deploy

on:
    pull_request:
        branches: [ master ]

jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2
            - name: Use Node.js
              uses: actions/setup-node@v1
              with:
                node-version: 12
              run: yarn install
              run: yarn build
              run: yarn test
            - name: Push build to S3
              uses: sai-sharan/aws-s3-sync-action@master
              with:
                access_key: ${{ secrets.ACCESS_KEY }}
                secret_access_key: ${{ secrets.SECRET_ACCESS_KEY }}
                region: 'us-east-1'
                source: 'build'
                destination_bucket: ${{ secrets.DESTINATION_BUCKET }}
                destination_prefix: ${{ secrets.DESTINATION_PREFIX }}
                exclude: '.git/*'
                delete: true
                quiet: false
```

## Usage:

The `aws-s3-sync-action` takes the following parameters as inputs:

|Key|Description|Type|Default|Required|
|---|-----------|----|-------|--------|
|access_key|Access key of a user with necessary S3 permissions|string|`None`|True|
|secret_access_key|Secret access key of a user with necessary S3 permissions|string|`None`|True|
|region|Region in which the bucket was created|string|`us-east-1`|False|
|source|Source directory/prefix that you want to sync|string|Entire workflow directory|False|
|destination_bucket|Destination S3 bucket where you want to sync the source|string|`None`|True|
|destination_prefix|S3 prefix in the destination bucket where you want to sync the source|string|`None`|False|
|exclude|Exclude all files or objects from the command that matches the specified pattern.|string|`None`|False|
|delete|Files that exist in the destination but not in the source are deleted during sync.|boolean|`true`|False|
|quiet|Does not display the operations performed from the specified command.|boolean|`false`|False|

## Suggestions:

- `access_key`, `secret_access_key` are confidential/sensitive information and you would not want them to be public. Suggestion is to add these values as [encrypted secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) and pass the secrets context to the inputs of `aws-s3-sync-action`

- `destination_bucket`, `destination_prefix` and even `source`(sometimes) may be confidential information. You can also add values for these inputs as encrypted secrets and pass the secrets context to the inputs of `aws-s3-sync-action`

Example:

```yaml
uses: sai-sharan/aws-s3-sync-action@master
with:
    access_key: ${{ secrets.ACCESS_KEY }}
    secret_access_key: ${{ secrets.SECRET_ACCESS_KEY }}
    region: 'us-east-1'
    source: ${{ secrets.SOURCE }}
    destination_bucket: ${{ secrets.DESTINATION_BUCKET }}
    destination_prefix: ${{ secrets.DESTINATION_PREFIX }}
    exclude: '.git/*'
    delete: true
    quiet: false
```  

## License

MIT License

Copyright (c) 2020  Sai Poona

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

