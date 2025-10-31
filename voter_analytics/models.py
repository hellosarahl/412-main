'''models.py for the voter_analytics project
File:models.py 
Name:Sarah Lam
Description: Models for view voters '''
from django.db import models
from datetime import datetime

# Create your models here.
#states and rep data from the marathon class
class Voter(models.Model):
    #identifiation and storing for the data of the voter in Newton
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    street_number=models.CharField(max_length=30)
    street_name=models.CharField(max_length=100)
    apt_number=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=10)
    birth=models.DateField()
    #dates
    date_reg=models.CharField(max_length=20)
    party_aff=models.CharField(max_length=2)
    precinct=models.IntegerField()

    #to give the voter participation or not
    v20state=models.BooleanField()
    v21town=models.CharField(max_length=100)
    v21primary=models.CharField(max_length=100)
    v22general=models.BooleanField()
    v23town=models.BooleanField()
    voter_score=models.IntegerField()


    def __str__(self):
      '''return string rep of the model instance'''
      return f"{self.first_name} {self.last_name}"
    
   # def get_voters_passed(self):
      # '''returns the number of votes passed by this person'''
     #  start_first=Result.objects.filter(start_time_of_day__lt=self.start_time_of_day)
     #  passed=start_first.filter(finish_time_of_dat_gt=self.finish_time_of_day)

     #  return len(passed)
    
    #def get_voters_passed_by(self):
     #  '''return the number of voters '''
      # started_later=Result.objects.filter(start_time_of_day__gt=self.start_time_of_day)
       #passed_by=started_later.filter(finish_time_of_day__lt=self.finish_time_of_day)

      # return len(passed_by)

       
    





    
    '''load data for processing the csv data file and load voter into django'''
    def load_data():
       #function to load data records
       #location of filename
       #dangerous
   
       filename='/Users/sarah/Desktop/newton_voters.csv'
       #open file for reading 
       f=open(filename,'r')
       #disregard header
       f.readline()

       #read the files 
       for line in f:
          fields=line.strip().split(',')
          try:
              #create new instance of result object with record from csv
              voter=Voter(
                          last_name=fields[1],
                          first_name=fields[2],
                          street_number=fields[3],
                          street_name=fields[4],
                          apt_number=fields[5],
                          zip_code=fields[6],
                           birth=datetime.strptime(fields[7],"%Y-%m-%d").date(),
                           date_reg=fields[8],
                             party_aff=fields[9],
                           precinct=int(fields[10]), 
                           v20state=fields[11]=='True',
                           v21town=fields[12],
                           v21primary=fields[13]=='True',
                           v22general=fields[14]=='True',
                           v23town=fields[15]=='True',
                           voter_score=int(fields[16]))
         
          #create new instance of result object with record from csv
              voter.save()
              print(f'Created voter:{voter}')
          except Exception as e:
             print(f"Skipped:{fields} due to {e}")
       print(f'Done.Created {len(Voter.objects.all())}Voters.')
          




          


       
       










