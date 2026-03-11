output "user_arn" {
  value = aws_iam_user.user.arn
}

output "group_arn" {
  value = aws_iam_group.group.arn
}

output "role_arn" {
  value = aws_iam_role.role.arn
}

output "iam_user_arns" {
  value = [for user in aws_iam_user.users : user.arn]
}

output "iam_user2_arns" {
  value = [for user in aws_iam_user.users2 : user.arn]
}
