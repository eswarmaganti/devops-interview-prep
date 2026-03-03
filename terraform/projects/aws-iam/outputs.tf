output "user_arn" {
  value = aws_iam_user.user.arn
}

output "group_arn" {
  value = aws_iam_group.group.arn
}

output "role_arn" {
  value = aws_iam_role.role.arn
}
