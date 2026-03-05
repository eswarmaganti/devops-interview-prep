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


# a list of iam users
variable "iam_users" {
  type    = list(string)
  default = ["bob", "john", "alan"]

  validation {
    condition     = alltrue([for user in var.iam_users : length(user) > 2 && length(user) <= 20])
    error_message = "IAM user account name should contain at least 3 characters long"
  }
}
