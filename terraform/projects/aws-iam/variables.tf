variable "iam_user" {
  description = "IAM user name"
  type        = string
  default     = "ansible"
}

variable "iam_group" {
  description = "IAM group name"
  type        = string
  default     = "devops"
}

variable "iam_role" {
  type        = string
  default     = "ec2_role"
  description = "IAM role name"
}
