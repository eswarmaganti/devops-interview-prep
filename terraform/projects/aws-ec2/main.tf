# defining data block to fetch the AMI id
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}

data "aws_ami" "ubuntu_ap" {
  provider = aws.ap
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}


# creating a S3 bucket
# resource "aws_s3_bucket" "bucket" {
#   bucket = "my-bucket-05032026"
# }

resource "aws_instance" "ec2_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  # depends_on = [ aws_s3_bucket.bucket ]
}

resource "aws_instance" "ec2_server_ap" {
  provider      = aws.ap
  instance_type = "t3.micro"
  ami           = data.aws_ami.ubuntu_ap.id
}
