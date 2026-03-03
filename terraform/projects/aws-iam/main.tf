
# creating an IAM user
resource "aws_iam_user" "user" {
  name = var.iam_user
  path = "/"

  tags = {
    "Env" = "dev"
  }
}

# Creating an IAM group
resource "aws_iam_group" "group" {
  name = var.iam_group
  path = "/"
}

# adding the IAM user to IAM group
resource "aws_iam_user_group_membership" "group_member" {
  user = aws_iam_user.user.name
  groups = [
    aws_iam_group.group.name
  ]
}

# Creating the IAM policy 
resource "aws_iam_policy" "policy" {
  name        = "AllowS3Readonly"
  path        = "/"
  description = "Allow the readonly access to S3"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowS3Readonly"
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:GetObjectVersion",
          "s3:ListBuckets",
          "s3:GetBucketPolicy",
          "s3:GetBucketLocation"
        ]
        Resource = "*"
      }
    ]
  })

  tags = {
    "Env" : "dev"
  }
}

# Attaching the IAM Policy to IAM Group
resource "aws_iam_group_policy_attachment" "policy_attachment" {
  group      = aws_iam_group.group.name
  policy_arn = aws_iam_policy.policy.arn
}


# Creating IAM Role
resource "aws_iam_role" "role" {
  name = var.iam_role
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "EC2Role"
        Effect = "Allow"
        Action = "sts:AssumeRole"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Name = "Ec2Role"
  }
}

# Cresting IAM role policy
resource "aws_iam_role_policy_attachment" "rol_policy_attachment" {
  role       = aws_iam_role.role.name
  policy_arn = aws_iam_policy.policy.arn
}

