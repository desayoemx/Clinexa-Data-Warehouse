resource "aws_s3_bucket" "staging-bucket" {
  bucket        = clinexa-staging
  force_destroy = true

  tags = {
    Name        = "Staging bucket"
    Environment = "Test"
  }
}






