# concurrent-programming

You will be downloading GIFs for flags from all the countries in the world from a public CIA website. The files appear in the following folder: 

https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/

Note: The web folder above is protected so you’ll get a 404 error if you try to read the page directly. If you add the file name to the URL, it works fine.

The names of the files have the following form: 
xx-lgflag.gif

where xx stands for the 2-character country code. For example, the GIF for the United States is us-lgflag.gif. The codes are in the file flags.py.

Write three similar scripts that do the following: 
-	Download all flag files into a directory named flags 
-	Report the number of bytes downloaded 
-	Report the execution time of the script (time.time()) 
-	Report the CPU time of the script (time.process_time()) 

The three versions will use the following schemes for downloading: 
1.	Download sequentially (no concurrency) seq.py 
2.	Download concurrently using futures with processes fprocess.py 
3.	Download concurrently using futures with threads fthread.py 
