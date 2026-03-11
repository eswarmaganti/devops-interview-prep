# Identity and Access Management (IAM)

AWS IAM is a web service that helps you securely control access to AWS resources. With IAM, you can manage permissions that control which AWS resources users can access.

You use IAM to control who is authenticated and authorized tro use resources. IAM provides the infrastructure necessary to control authentication and authorization for your AWS accounts.

### IAM Users
- **Definition**: Represents a person or service that interacts with AWS
- **Credentials**: username/password for the console, access keys for API/CLI
- **Permissions**: New users have no permissions by default; they must be assigned via policies or groups
- **Use Case**: IAM users are ideal for administrators who need access to AWS Management Console or specific users who require access to a subset of AWS resources.

### IAM Groups
- **Definition**: A collection of IAM users. Groups are used to manage permissions for multiple users at once.
- Simplifies the permission management by attaching by allowing policies to be attached to the groups instead of individual users
- A user can belongs to multiple groups. A group can have multiple policies attached.

### IAM Policies
- A JSON document that defines permissions, specifying which actions are allowed or denied on which resource.
- Policies are the rules that dictate what a user, group or a role can do.
- **Types**:
  - **Identity-based policies**: Attached to users, groups or roles
  - **Resource-based Policies**: Attached directly to resources like S3 buckets
  - **Service Control Policies (SCPs)**: Set maximum permissions for account members in an organization.

Basic Structure of IAM policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "StatementName",
      "Effect": "Allow",
      "Action": "service:action",
      "Resource": "arn:aws:service:region:account-id:resource"
    }
  ]
}
```
- **Version**: specifies policy language version, defaults to `2012-10-17`
- **Statement**: It's an array of statements. A policy can have multiple statements. Each statement defines one permission rule
- **Effect**: Two possible values, "Allow/Deny"
- **Action**: Defines what operation is allowed/denied
- **Resource**: Defines which AWS resource the action applies to

Example IAM policy to provide full access to S3
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3AccessToGroup"
      "Effect": "Allow",
      "Resource": "*",
      "Action": "s3:*"
    }
  ]
}
```

### IAM Role
- An identity with specific permissions that is not attached to a single person but can be assumed by anyone(user), application, ot service that needs temporary access. 
- Roles are ideal for cross account access or service-to-service interaction

IAM Role has two policy documents
1. Trust Policy (Who can assume the role)
2. Permission Policy (What can the role do after assuming)

EX: Trust Policy 
```json
{
  "Version": "2012-10-17",
  "Statement":[
    {
      "Sid": "AllowEC2AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
        # "AWS": "<ARN>" - for another aws account 
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

EX: Permission Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3Access",
      "Effect":"Allow",
      "Action":"s3:*",
      "Resource": "*"
    }
  ]
}
```