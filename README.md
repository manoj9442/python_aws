# python_aws
Create EC2 instance using Boto3

 What is EC2 On-Demand instance?
 
     This is one of a pricing model based EC2 instance which we usually create.
     There is no time commitment and no advance payment. 
     We need to pay only for hours we used.
     Highest cost as there is no time commitment.
     
What is EC2 Reserved Instance (RIs)?

     This is also one of pricing model based EC2 instance and can get upto 75% discount over On-Demand instance.
     There is a time commitment.we can buy it for a time frame like 1 year or 3 year.
     It will apply automatically on On-Demand insatnce if we use any of same configuraton or we can purchase seprately.
     There are three payment option like All Upfront, Partial Upfront and No Upfront.
     There are three types of RIs as following:
        1. Standard : We can get discount upto 72% over On-Demand Insatnce and can some limited modification like instance size, availabity zone.
        2 Converitible : We can get discount upto 54% over On-demand Insatnce and can change instance family, payment option, operating system, tenancy.
        3. Schedule : This option allow us to match capicity reservation to a predictable schedule that only requires fraction of the a day, a week, a month.
        
        
 How to convert On-Demand Instance into a Reserved Instance?
 
      We can purchase Reserved instance from console and it will also apply automatically to on-demand instance if we are using any of same configuration of RIs.
      
      To convert On-Demand instance into Reserved instance, ensure that we specify following information in the configuaration of On-Demand:
      Platfrom: We must specify an AMI that matches the platform of RIs.
      
      Instance Type: We must specify same instance type as Your Reserved Instance.
      
      Availability Zone: We must launch instance in same availabe  zone.
      
      Tenancy : The tenancy of instance must match tenancy of our reserved instance.
      
      Instance Size Flexibility: With Instance size flexibility, the reserved instance discount applies to instance usage within the instance family. The Reserved instance applied from smallest to  largest instance size within instance family based on normalization factor. Instance Size flexibility applies only to Regional insatnces. Instance size flexibility is determined by normalization factor of instance size. For Example, a t2.medium instance has a normalization factor of 2. If you purchase a t2.medium reserved instance and you have two t2.small insatnces are running then benefit of billing is applied in full on both instances or if you have one t2.large insatnce running then billing benefit is applied to 50% of the usage of the insatnce.
      
      
     
     
