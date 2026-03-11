terraform {
  required_providers {
    aws = {
      version = "~>6.0"
      source  = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

provider "aws" {
  alias   = "ap"
  region  = "ap-south-1"
  profile = "default"
}
