''' one of the many ways of reading and counting term frequencies 
in python.  In any "full text information retrieval", big data, 
data mining/text mining activities, we start by reading files and 
counting the frequencies of the "tokens" - the words - hence the big 
bag of words.  This is an example, perhaps covering more than we have 
so far in our class, that reads a file, communicates a LOT with the end 
user and then counts words.  

Notice that this script doesn't use one of the handy python libraries,
 such as counter (which is what I used in the demo for class).  
 
As a final touch to this example, I'll add notes in the body of the script.
(from https://stackabuse.com/read-a-file-line-by-line-in-python/)

-- NOTE: I'M USING ALL CAPS FOR LEGIBILITY; IN PRACTICE, PLEASE DON'T.
'''

''' SINCE WE'RE CHECKING THE EXISTENCE OF FILES AND USING THE 
FULL PATH TO THAT FILE, LET'S INCLUDE THE APPROPRIATE LIBRARIES - 
sys and os
'''
import sys
import os

def main():
	''' THE MAIN STATEMENT - ALL SCRIPTS/PROGRAMS NEED A FRONT-DOOR...
	AND THE CONVENETION IS TO USE "MAIN"
   filepath = sys.argv[1]

   if not os.path.isfile(filepath):
   		''' NOTICE THIS STATEMENT CHECKS THE FULL PATH - DONT HARD
   		CODE, E.G., c:\\myDocs... IN A FILE - ASK THE SCRIPT TO ASK 
   		THE OPERATING SYSTEM FOR THE PATH. '''
   		
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   bag_of_words = {}
   ''' IN FULL-TEXT RETRIEVAL THE JOKE IS THE BIG BAG OF WORDS ...
   SO THATS WHAT WERE GETTING READY FOR ... NOTE, TOO, THAT USUALLY WE 
   SKIP STOP WORDS - WORDS WITH SUCH FREQUENCY THAT THE DONT HELP 
   TO DISCRIMINATE AND BECOME JUST NOISE.'''
   
   with open(filepath) as fp:
   		''' THE fp IS THE FILE POINTER - THE OS HANDS THE SCRIPT
   		A WAY OF READING THE FILE.'''
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
           ''' NOTICE:  LINE 49 USES THE .format() FOR OUTPUT - BUT THERE
           ARE MANY WAYS TO PRINTING W/ PYTHON '''
           ''' NOTE, TOO, THE USE OF THE MULTIPLE METHODS APPENDED 
           TO CLEAN UP THE LINE. ''' 
           
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   print("Most frequent 10 words {}".format(sorted_words[:10]))
   ''' GOOD OL SPLICER WITH : '''
  
def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)
   ''' NOTICE THE USE OF LAMBDA -IN- THE RETURN STATEMENT '''
   

def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1

if __name__ == '__main__':
	''' JOY - GOOD CODE DEFINES ALL THE FUNCTIONS/CLASSES AHEAD OF TIME 
	AND ONLY WHEN ALL iS CHECKED AND READY TO GO IS WHEN WE START THE PROGRAM.
	BTW, THE __ IS CALLED A DUNDLE (DOUBLE UNDERSCORE) AND SIGNALS TO PYTHON 
	THE USE OF MAGIC METHODS.'''
   main()