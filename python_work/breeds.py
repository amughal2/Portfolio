import csv


from matplotlib import pyplot as plt


#get dates, high, and low temperatures from file.
filename = 'breed_Info.csv'
with open (filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	

	highs, lows = [], []
	for row in reader:
		try:
			
			high = int(float(row[2]))
			low = int(float(row[1]))
		except ValueError:
			print(current_date, 'missing data')
		else:
			
			highs.append(high)
			lows.append(low)
		

	print(highs)

#Plot data.
fig = plt.figure(dpi = 128, figsize =(10,6))
plt.plot(highs, c='red', alpha=0.5)
plt.plot(lows, c='blue', alpha=0.5)
plt.fill_between(highs,lows, facecolor='blue', alpha=0.1)

#format Plot
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis ='both', which='major', labelsize = 16)

plt.show()