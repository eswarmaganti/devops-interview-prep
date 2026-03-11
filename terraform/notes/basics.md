## Infrastructure as Code (IaC)
Infrastructure as Code (IaC) is the managing and provisioning of infrastructure through code instead of manual processes.
With IaC, configuration files are created that contain your infrastructure specifications, which makes it easier to edit and distribute configurations. It also ensures that you provision the same environment every time.

### Key Aspects and Benefits of IaC
- **Automation & Speed**: Infrastructure can be spun up or torn down rapidly, reducing manual labour
- **Consistency**: Eliminates configuration drift by ensuring the exact same environment is provisioned every time.
- ** Version Control**: Configuration files stored in systems like Git, allowing tracking, auditing, and collaboration on infrastructure.
- **Approaches**:
  - **Declarative**: You define the desired end-state and the tool decides how to achieve it.
  - **Imperative**: You define the specific commands to achieve the desired state.

### Core Terraform Workflow
The core Terraform workflow has three steps:
1. **Write** - Author Infrastructure as code
2. **Plan** - Preview changes before applying
3. **Apply** - Provision reproductive infrastructure

#### Write
- **Define Infrastructure**: Author infrastructure configurations using the HashiCorp Configuration Language (HCL) in `.tf` files. This declarative code describes the desired end state of your infrastructure.
- **Initialize**: Run the `terraform init` command in your project directory. This command prepares the working directory by downloading necessary provider plugins and modules and setting up the state backend.

#### Plan
- **Preview Changes**: Execute `terraform plan` to create an execution plan. Terraform compares your configuration to the current infrastructure state and displays a description of the changes necessary to achieve the desired state.
- **Review**: The plan output serves as a preview and a crucial step for peer review to ensure the changes are expected and compliant before any real infrastructure affected.

#### Apply
- **Provision**: Run `terraform apply` to execute the actions proposed in the plan. We can bypass the prompt for approvals by passing `--auto-approve` option to the above command
- **Monitor and Iterate**: Terraform carries out the operations in the correct order, respecting the resource dependencies.

#### Additional commands
- `terraform validate`: Checks if the configuration is syntactically valid and internally consistent, without accessing remote infrastructure or state.
- `terraform destroy`: Creates a plan to tear down all resources manages by the current configuration and prompts for confirmation before permanently deleting them.
- `terraform fmt`: Automatically formats your HCL code for consistency.

---

## File Structure in Terraform
Terraform project typicaly utilize several standard files to organize infrastructure as code. While you can put all configuration in a single `.tf` file, best practices recommend separating them for better readability and maintanance.

The main files in a Terraform project include:
- `main.tf`: The file is the primary entry point for the module and contains the core infrastructure configuration, including resource definitions, data sources and module calls.
- `variables.tf`: This file is where all input variables for configuration are declared and documented, making the configuration dynamic and reusable.
- `outputs.tf`: This file defines the output values, which are used to display information about the provisioned infrastructure or pass data to other configurations.
- `providers.tf`: This optional file centralizes the configuration for required providers and their specific settings like region and authentication.
- `terraform.tfvars`: This file is used to assign values to the variables declared in `variables.tf`. It's an optional file and often excluded from version control if it contains sensitive information.
- `.terraform.lock.hcl`: This file is automatically created during `terraform init` and locks the provider versions to ensure consistency across different environments and team members. It should be committed to version control.
- `terraform.tfstate`: This file (or remote storage) is where terraform stores the state of your managed infrastructure, mapping real-world resources to your configuration. It is crucial for Terraform to understand the current infrastructure and should not be manually edited or committed to version control.

Terraform treats all the `.tf` files in a directory as single configuration, regardless of their individual names, merging them alphabetically. This allows for logical grouping of resources.

---

## Providers in Terraform
A Terraform provider is a plugin that acts as an intermediary enabling Terraform to communicate with external APIs - such as AWS, Azure, GCP or SaaS tools to create, update and delete infrastructure.
These plugins translate terraform code into API requests, allowing for standardized management of resources across diverse technologies.

Key aspects of Terraform providers include:
- **Plugin Architecture**: Providers are distributed separately from Terraform, allowing them to have their own versioning and release cycles.
- **Functionality**: They define resource types (e.g., `aws_instance`) and data sources (e.g., `azurerm_resource_group`).
- **Categories**: Providers are categorized as Official (maintained by hashicorp), Partner (maintained by vendors like Datadog), orr Community (open-source).
- **Configuration**: They must be declared in Terraform code to tell Terraform which APIs to use, typically with authentication details or regional settings.
- **Examples**: Common providers include `aws`, `azurerm`, `google`, `kubernetes` and `random`

### How to use providers
Using a provider in Terraform involues declaring the required provider, optionally configuring it, and then running the standard terraform workflow commands.

#### 1. Declare provider requirements
In your terraform configuration files, you must specify which providers your configuration requires within a `terraform` block and a nested `required_providers` block

```hcl
terraform{
  required_providers{
    # the key "aws" is local name
    # the source identifies the provider in the registry
    # The version constraint ensures consistent behavior across multiple runs
    aws = {
      version = "~>6.0"
      source = "hashicorp/aws" 
    }
  }
}
```
#### 2. Configure the providers
Use a `provider` block to configure provider-specific settings, such as the cloud region or authentication details. If you omit this block, terraform will use the an empty, default configuration.
```hcl
providers {
  region = "us-east-1"
  profile = "default"
}
```

### Using multiple providers
To use multiple providers in Terraform, you define multiple `provider` blocks and use the `alias` meta-argument to distinguish the non-default configuration.You can then specify which provider configuration a resource should use with the `provider` meta-argument. 

This is useful for multi-cloud deployments, deploying resources to multiple regions/accounts, or managing different layers of an application within a single configuration.

#### 1. Declare required providers
```hcl
terraform{
  required_providers{
    aws = {
      source = "hashicorp/aws"
      version = "~>6.0"
    }

    # Declare other providers like azurerm, gcp etc.
  }
}
```
#### 2. Configure providers with aliases
- For different cloud providers: simply define separate provider blocks for each
- For multiple configuration for same provider: use the `alias` meta-argument

```hcl
# the default provider
provider "aws" {
  region = "us-east-1"
}

# defining the same provider for another region
provider "aws" {
  alias = "eu"
  region = "eu-west-1"
}

# defining a different provider
provider "azurerm"{
  features {}
}
```

#### 3. Assign resources to specific providers

```hcl
resource "aws_s3_bucket" "bucket_us" {
  bucket = "my_bucket_us"
}

resource "aws_s3_bucket" "bucket_eu" {
  provider = aws.eu
  bucket = "my_bucket_eu"
}
```

---

## Resources in Terraform
A Terraform resource is a configuration block that defines a piece of infrastructure you want to manage, such as a virtual machine, a network, or a database.

It acts as the primary building block if Terraform configurations and is managed through its lifecycle

### Key components of a resource
1. `resource` keyword: Declares the block type
2. **Resource Type**: Specifies the kind of infrastructure object, such as `aws_instance` for an EC2 instance or `aws_s3_bucket` for an S3 bucket. The type is determined by the specific provider you are using.
3. **Logical Name**: A unique identifier you can assign for internal use within your Terraform configuration. It does not affect the actual name of the infrastructure object in the cloud provider.
4. **Arguments**: These are specific settings that configure the behavior and properties of the infrastructure object itself (e.g., `ami` and `instance_type` for an EC2 instance). These are defines by the provider.
5. **Meta-arguments**: These are built-in to the Terraform language and control how Terraform manages the resources, such as `count`, `for_each` and `lifecycle`
6. **Attributes**: Terraform resource attributes are values that are exported by a resource after it is created or updated by the cloud provider. Unlike arguments, which you configure, attributes are assigned by the provider and are used to reference once the resource in the configuration of another.

Example
```hcl

# a resource to create an IAM user in AWS
resource "aws_iam_user" "user" {
  name = "test-user"
  path = "/users/"

  tags = {
    Environment = "testing"
  }
}

# Accessing the attributes
output "user_arn" {
  value aws_iam_user.user.arn
}
```

---

## Variables in Terraform
Terraform variables are used to parameterize configurations, allowing values to be passed in from external sources without hardcoding them into the main configuration files. This makes infrastructure code more flexible, reusable, and maintainable across different environments.

### Declaring a variable
Variables are declared using a `variable` block, typically in a dedicated file named `variables.tf`

```hcl
variable "iam_user"{
  type = string
  description = "Name of the IAM user"
  default = "john"
  validation {
    condition = length(var.iam_user) > 2
    error_message = "IAM user name should be at least 3 characters long"
  }
}
```
- **type**: Specified the type of value the variable accepts (e.g., `string`, `bool` ..)
- **description**: A description of the variable's purpose, which helps other users understand how to use it.
- **default**: A default value, making the variable optional. If no default is provided, the user must supply a value.
- **validation**: A optional block to enforce specific rules on the variable's value. which helps catch configuration errors early.
- **sensitive**: setting this to `true` prevents te value from being displayed in CLI output, although it is still stored in the state file.

### Using variables
Variables are referenced within the configuration using the `var.<variable_name>`

```hcl
resource "aws_iam_user" "user" {
  name = var.iam_user
  path = "/users/"
}
```

### Assigning values to Variables
Values can be assigned in multiple ways, in a specific order of precedence (lowest to highest)
1. `default` **argument**: The value specified in the `variable` block itself.
2. `Environment variables`: Environment variable prefixed with `TF_VAR_` (e.g., `export TF_VAR_iam_name="bob"`)
3. `terraform.tfvars`: An automatically loaded file for storing variable values.
4. `*.auto.tfvars` **file**: Any files ending with `.auto.tfvars` (loaded in lexical order)
5. `-var-file` **Commandline flags**: Explicitly specified files using `terraform apply -var-file="production.tfvars"`
6. `-var` **command inline flags**: Values specified directly on the command line using `terraform apply -var="i=iam_user=jose" (highest precedence for CLI workflows)

---

## Data Blocks in Terraform
Terraform `data` blocks are used to fetch data about pre-existing or external resources for use within your configuration, without managing the lifecycle of those external resources.

### Key Concepts
- **Read-Only**: Unlike `resources` blocks, which manage infrastructure, `data` blocks are purely read-only. They query information from a provider's API(AWS, Azure, etc.), other Terraform states, local files, or HTTP endpoints.
- **Dynamic Configuration**: They allow your configuration to be dynamic and avoid hardcoding values that might change, such as most recent machine image (AMI) ID or a default VPC's ID.
- **Execution Order**: Terraform attempts to query data sources during the plan phase, but if any of the arguments rely on values that are only known during the apply phase, the read operation is deferred until apply time.

Syntax
```hcl
data "<type>" "<label>" {
  # configuration arguments
  # meta arguments
}
```

## Meta-Arguments in Terraform
Meta arguments are a class of arguments built into the Terraform Configuration language that control how Terraform creates and manages your infrastructure. You can use meta-arguments in any type of resource. You can also use most meta-arguments in `module` blocks.

### `depends_on`
The depends_on meta-argument instructs Terraform to complete all actions on the dependency object, including `read` operations, before performing actions on the object declaring the dependency.
We can use the `depends_on` argument explicitly set the order in which Terraform creates resources.

### `count`
By default, Terraform configures one infrastructure object for each `resource`, `module` and `ephemeral` block. Terraform also creates single instances of a module per `module` block. 
You can add the `count` argument to `resource`, `module` and `ephemeral` blocks to create and manage multiple instances of each without writing a separate block for each instance.

Creating multiple users using count argument
```hcl
variable iam_users {
  type = string
  default = ['bob', 'alice', 'john']
  description = "List of IAM user account names"

  validation = {
    condition = alltrue([for user in var.iam_users : length(user) > 2 && length(user) < 20 ])
    error_message = "The IAM user account name should be at least 3 character's long"
  }
}

resource "aws_iam_user" "user" {
  count = length(var.iam_users)
  name = var.iam_users[count.index]
  path = "/users"
}
```

### `for_each`
By default, Terraform configures one infrastructure object for each `resource`, `module` and `ephemeral` block. 

You can add the `for_each` block to your `resource`, `data`, `module` and `ephemeral` blocks to create and manage several similar objects, such as a fixed pool of compute instances, without writing a separate block for each instance.

Example

```hcl

variable "iam_users" {
  type = string
  default = ['bob', 'alice', 'john']
}

resource "aws_iam_user" "users" {
  for_each = toset(var.iam_users)
  user = each.value
  path = "/users/"
}

```

### `lifecycle`
The lifecycle meta-argument allows us to control how Terraform manages a resource during its lifecycle, such as when the resource is created, updated, or destroyed.

By default, Terraform decides how to modify infrastructure when changes are made in the configuration. However, in some situations we may want to customize this behavior to avoid downtime or protect critical resources. This is where the lifecycle block becomes useful.

**Scenario**: Imagine you have an AWS EC2 instance running a production application. 
- If you modify certain parameters in the Terraform configuration, Terraform may need to destroy the existing instance and create a new one.
- If Terraform destroys the instance first and then creates the new one, it could cause application downtime.
- Using the lifecycle block, we can change this behavior and instruct Terraform to create the new resource first and then destroy the old one, ensuring minimal disruption.

### `provider`
By default, Terraform determines the local name of the provider from the first word in the resource type and used that provider's default configuration to create the resource.

You can add multiple `provider` blocks to your configuration and use the `provider` argument to a resource definition to specify which provider

```hcl
# defining providers
provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

provider "aws" {
  alias   = "west"
  region  = "us-west-1"
  profile = "default"
}


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

resource "aws_instance" "ec2_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  # depends_on = [ aws_s3_bucket.bucket ]
}

resource "aws_instance" "ec2_server_ap" {
  provider      = aws.ap
  instance_type = "t3.micro"
  ami           = data.aws_ami.ubuntu.id
}
```

### `providers`
By default, when we use a child module, Terraform automatically uses the default provider configuration defined in the parent module. This means any resources created inside the child module will be provisioned using the same provider settings unless we explicitly override them.
The providers meta-argument inside the module block allows us to specify which provider configuration the module should use.
This is useful when deploying resources across multiple regions or accounts using the same module.

---

## Terraform State
The Terraform state file is **a crucial component that acts as the source of truth** for your infrastructure managed by terraform.

It maps the resources defined in your configuration files (written in HCL) to the actual real-world objects deployed in your cloud or on-premises environment.

### Key purpose
- **Mapping Resources**: It tracks the unique identifiers (like instance IDs, IP addresses) of real resources created, binding them to their definitions in the configuration.
- **Performance Optimization**: It stores a cache of resource attributes, which allows Terraform to create execution plans efficiently without needing to query the cloud provider for the complete current state of every resource before every operation.
- **Dependency Tracking**: The state file retains metadata about resource dependencies, which helps Terraform determine the correct order for creation, updating or destroying resources, even if a resource is removed from the configuration.
- **Drift Detection**: By comparing the current configuration with the state file and the actual infrastructure, Terraform can detect "drift" and plan to reconcile it.

### Storage and Management
- **Local Storage**: By default Terraform stores the state in a local file named `terraform.tfstate` in the directory where it is run. This is suitable for personal use or testing.
- **Remote Storage**: For team collaboration and production environments, storing state locally is problematic. The recommended approach is to use a **remote backend** like HCP Terraform, Amazon S3, Azure Blob Storage etc.
- **State Locking**: Fully-featured remote backends support state locking to prevent multiple users from making changes to the same state file simultaneously, which helps prevent corruption and conflicts.
- **Security**: The state file can contain sensitive information (like passwords & access keys), so it must be stored securely, encrypted at rest, and access should be strictly limited to authorized personal. It should never be committed to a version control system like Git.

### Interacting with Terraform State
While the state file is in JSON format, **manual editing is strongly discouraged** due to the risk of data corruption or creating discrepancies between the state and the real infrastructure.
Indeed you can use the `terraform state` CLI commands for advanced management.

- `terraform state list`: Lists all resources currently tracked in the state
  ```bash
  $ terraform state list
  data.aws_ami.ubuntu
  data.aws_ami.ubuntu_ap
  aws_instance.ec2_server
  aws_instance.ec2_server_ap
  ```
- `terraform state show [address]`: Displays the details and attributes of a specific resource in the state file
  ```bash
  $ terraform state show aws_instance.ec2_server
  # aws_instance.ec2_server:
  resource "aws_instance" "ec2_server" {
      ami                                  = "ami-0071174ad8cbb9e17"
      arn                                  = "arn:aws:ec2:us-east-1:781167327996:instance/i-02bba6bc0e169175e"
      associate_public_ip_address          = true
      availability_zone                    = "us-east-1f"
      disable_api_stop                     = false
      disable_api_termination              = false
      ebs_optimized                        = false
      force_destroy                        = false
      get_password_data                    = false
      hibernation                          = false
      host_id                              = null
      iam_instance_profile                 = null
      id                                   = "i-02bba6bc0e169175e"
      instance_initiated_shutdown_behavior = "stop"
      instance_lifecycle                   = null
      instance_state                       = "running"
      instance_type                        = "t3.micro"
      ipv6_address_count                   = 0
      ipv6_addresses                       = []
      key_name                             = null
      monitoring                           = false
      outpost_arn                          = null
      password_data                        = null
      placement_group                      = null
      placement_group_id                   = null
      placement_partition_number           = 0
      primary_network_interface_id         = "eni-0d2086913b6cee496"
      private_dns                          = "ip-172-31-64-21.ec2.internal"
      private_ip                           = "172.31.64.21"
      public_dns                           = "ec2-3-237-16-228.compute-1.amazonaws.com"
      public_ip                            = "3.237.16.228"
      region                               = "us-east-1"
      secondary_private_ips                = []
      security_groups                      = [
          "default",
      ]
      source_dest_check                    = true
      spot_instance_request_id             = null
      subnet_id                            = "subnet-0837ac62052bc46fb"
      tags_all                             = {}
      tenancy                              = "default"
      user_data_replace_on_change          = false
      vpc_security_group_ids               = [
          "sg-071831f9bfc9b3801",
      ]

      capacity_reservation_specification {
          capacity_reservation_preference = "open"
      }

      cpu_options {
          amd_sev_snp           = null
          core_count            = 1
          nested_virtualization = null
          threads_per_core      = 2
      }

      credit_specification {
          cpu_credits = "unlimited"
      }

      enclave_options {
          enabled = false
      }

      maintenance_options {
          auto_recovery = "default"
      }

      metadata_options {
          http_endpoint               = "enabled"
          http_protocol_ipv6          = "disabled"
          http_put_response_hop_limit = 2
          http_tokens                 = "required"
          instance_metadata_tags      = "disabled"
      }

      primary_network_interface {
          delete_on_termination = true
          network_interface_id  = "eni-0d2086913b6cee496"
      }

      private_dns_name_options {
          enable_resource_name_dns_a_record    = false
          enable_resource_name_dns_aaaa_record = false
          hostname_type                        = "ip-name"
      }

      root_block_device {
          delete_on_termination = true
          device_name           = "/dev/sda1"
          encrypted             = false
          iops                  = 3000
          kms_key_id            = null
          tags                  = {}
          tags_all              = {}
          throughput            = 125
          volume_id             = "vol-0bab3cd6e5bebee46"
          volume_size           = 8
          volume_type           = "gp3"
      }
  }
  ```

- `terraform state import [address] [ID]` Imports an existing, externally created resource into Terraform management and adds it to the state file.
- `terraform state rm [address]`: Removes a resource from rhe state file without destroying the actual remote resource.
- `terraform state mv [source] [destination]`: Moves a resource to a new address within the state, which is useful when refactoring configuration,

- `terraform state pull/push`: Manually download/upload state files, typically for advanced or recovery operations
  ```bash
  $ terraform state pull
  {
    "version": 4,
    "terraform_version": "1.14.6",
    "serial": 31,
    "lineage": "83ae3f6a-00a8-2f44-9540-2b6494a30d12",
    "outputs": {},
    "resources": [
      .
      .
      .

  }

  $ terraform state push
  ```

- `terraform refresh`
  ```bash
  $ terraform refresh
  data.aws_ami.ubuntu_ap: Reading...
  data.aws_ami.ubuntu_ap: Read complete after 0s [id=ami-0a14f53a6fe4dfcd1]
  data.aws_ami.ubuntu: Reading...
  data.aws_ami.ubuntu: Read complete after 1s [id=ami-0071174ad8cbb9e17]
  ╷
  │ Warning: Empty or non-existent state
  │ 
  │ There are currently no remote objects tracked in the state, so there is nothing to refresh.
  ╵
  ```