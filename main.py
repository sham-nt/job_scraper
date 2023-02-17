'''
Simple webscraper for fetching jobs 
with user inputs

Created by : @sham-nt (Shamanth Kashyap)
'''
import time
from func import *

def main():
    print("Enter the Programming language or skill you are familiar with: ")
    search_skill = input('>')
    print("Enter one/more language or skill you are unfamiliar with to filter out: ")
    unfamiliar_skill = list(input('>').split(" "))
    print('\n\n')
    while True:
        time_wait = 10
        #find_job1(search_skill, unfamiliar_skill)
        #find_job2(search_skill, unfamiliar_skill)
        find_job3(search_skill)
        print(f"Waiting every {time_wait} minutes...")
        time.sleep(time_wait * 60)
        
        
if __name__ == '__main__':
    main()