from django.db import models

class UserLogin(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)


class UserRegistration(models.Model):
    fullname=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    pincode = models.IntegerField()
    contact=models.IntegerField()
    email = models.CharField(max_length=20)

class BabyInfo(models.Model):
    year = models.CharField(max_length=20)
    childname = models.CharField(max_length=20)
    bloodgroup = models.CharField(max_length=20)
    Photo=models.FileField(upload_to='documents/',null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    doj = models.DateField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    adoption_status=models.CharField(max_length=50,null=True)

class ParentsInfo(models.Model):
    Applicant_name=models.CharField(max_length=50,null=True,blank=True)
    Husband_name=models.CharField(max_length=100,null=True,blank=True)
    spouse_name = models.CharField(max_length=100,null=True,blank=True)
    education=models.CharField(max_length=50,null=True,blank=True)
    occupation=models.CharField(max_length=50,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Photo=models.FileField(upload_to='documents/',null=True,blank=True)
    Marriage_certificate=models.FileField(upload_to='documents/',null=True,blank=True)
    Application_No = models.IntegerField(null=True,blank=True)
    parent_type = models.CharField(max_length=50,null=True,blank=True)
    aadhar_copy = models.FileField(upload_to='documents/', null=True, blank=True)

class Requeststatus(models.Model):
    appln_no=models.IntegerField(null=True,blank=True)
    requeststatus=models.CharField(max_length=40,null=True,blank=True)
    requestdate=models.DateField()
    adoptionstatus = models.CharField(max_length=40,null=True,blank=True)

class Homevstngstatus(models.Model):
    ApplnNo=models.IntegerField()
    visited_date=models.DateField()
    doc_verification=models.CharField(max_length=20)
    visiting_status=models.CharField(max_length=20)

class SurityInfo(models.Model):
    ApplnNo = models.IntegerField()
    Surity_amount = models.IntegerField()
    Surity_duration = models.CharField(max_length=20)
    terms_conditions = models.CharField(max_length=20)


class CharityInfo(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Contact_No = models.IntegerField()
    Email = models.CharField(max_length=20)
    Occupation = models.CharField(max_length=20)

class DonationInfo(models.Model):
    Charity_id = models.CharField(max_length=50,null=True,blank=True)
    Donation_Amt = models.IntegerField()
    Donation_things = models.CharField(max_length=20)
    Donation_date = models.DateField()
    purpes = models.CharField(max_length=20)

class OrphanageInfo(models.Model):
    Member_Name = models.CharField(max_length=20)
    Age = models.CharField(max_length=20)
    JoiningYear = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    guardian_name = models.CharField(max_length=20)

class OrphnHltSts(models.Model):
    Member_id = models.CharField(max_length=20)
    Health_problems = models.CharField(max_length=20)
    last_checkup_date = models.DateField()
    Previous_checkupdate = models.DateField()

class ParentReg(models.Model):
    fullname=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    pincode=models.IntegerField(null=True,blank=True)


class AdoptionRequest(models.Model):
    request_id=models.IntegerField()
    request_by=models.CharField(max_length=100)
    request_date=models.DateField()
    adoption_reason=models.CharField(max_length=200)
    occupation=models.CharField(max_length=100)
    family_members=models.CharField(max_length=20)
    annual_income=models.CharField(max_length=11)
    assets = models.CharField(max_length=200)
    status = models.CharField(max_length=30)
    baby_id=models.IntegerField(null=True,blank=True)
    photo = models.CharField(max_length=500,null=True, blank=True)


class OtpCode(models.Model):
    otp_code=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=40,null=True,blank=True)



# Create your models here.
