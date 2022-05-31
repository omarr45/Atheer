# -*- coding: UTF-8 -*-

from TAO_Arabic_Stemmer import TAOstemmer

string = 'وَقَفَ الطُّلابُ في صُفوفٍ مُرَتَّبَةٍ، ثُمَّ خَرَجوا إلى حَقْلٍ قَرِيبٍ. أَخَذوا مَعَهُمْ غِراسَ التّينِ والخَوْخِ، حَفَرَ الطُّلابُ الأَرْضَ وَزَرَعوا الغِرَاسَ، ثمَّ سَقَوْها المَاءَ. عادَ الطُّلابُ إلى المَدْرَسَةِ مسرورين.'

string = 'النفس تواقة إلى طلب العلم من منابعه ، و يظل الإنسان طالبا ً للعلم المفيد للدين وللمجتمع كليهما ما أمكنه ذلك في حاضره ومستقبله ، فمن يتخذ العلم نورا َ يستنر به في ظلمات تضله ، حتى يسمو إلى عالم أكثر تحضرا ً ، والوطن يحتضن الفائقين من أبنائه ، فيا طالب العلم ، كن معول بناء ليرقى الوطن ويتقدم'

string = 'رآها العصفور فحام حولها عدة مرات ثم حط إلى جانبها وقال: ما أكبر حبة الشعير هذه ! ابتسمت النملة الصغيرة مزهوة وقالت: ستفرح بها أمي كثيراً .'

# stems_list = TAOstemmer.text2stem(string, full=False)
stems_list = TAOstemmer.text2root(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word + '\n')

file.close()
