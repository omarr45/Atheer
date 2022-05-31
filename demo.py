import TAOstemmer

string = 'وَقَفَ الطُّلابُ في صُفوفٍ مُرَتَّبَةٍ، ثُمَّ خَرَجوا إلى حَقْلٍ قَرِيبٍ. أَخَذوا مَعَهُمْ غِراسَ التّينِ والخَوْخِ، حَفَرَ الطُّلابُ الأَرْضَ وَزَرَعوا الغِرَاسَ، ثمَّ سَقَوْها المَاءَ. عادَ الطُّلابُ إلى المَدْرَسَةِ مسرورين.'

# stems_list = TAOstemmer.text2stem(string, full=False)
stems_list = TAOstemmer.text2root(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word + '\n')

file.close()
