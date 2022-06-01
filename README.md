# ✨ Atheer

### Check the demo [here](https://www.atheer.ml)

<br>

## Atheer is an Arabic stemmer that provides two features, *STEM* and *ROOT*

![ScreenShot from Atheer.ml](https://user-images.githubusercontent.com/58887202/171515129-da6db888-81b7-4b3d-b384-ecf902e8f647.png)

<br>

## Example
"وَقَفَ الطُّلابُ في صُفوفٍ مُرَتَّبَةٍ، ثُمَّ خَرَجوا إلى حَقْلٍ قَرِيبٍ. أَخَذوا مَعَهُمْ غِراسَ التّينِ والخَوْخِ، حَفَرَ الطُّلابُ الأَرْضَ وَزَرَعوا الغِرَاسَ، ثمَّ سَقَوْها المَاءَ. عادَ الطُّلابُ إلى المَدْرَسَةِ مسرورين."

|FN| 27| 26| 25| 24| 23| 22| 21| 20| 19| 18| 17| 16| 15| 14| 13| 12| 11| 10| 09| 08| 07| 06| 05| 04| 03| 02| 01| 00|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|original| مسرورين.| المَدْرَسَةِ| إلى| الطُّلابُ| عادَ| المَاءَ.| سَقَوْها| ثمَّ| الغِرَاسَ،| وَزَرَعوا| الأَرْضَ| الطُّلابُ| حَفَرَ| والخَوْخِ،| التّينِ| غِراسَ| مَعَهُمْ| أَخَذوا| قَرِيبٍ.| حَقْلٍ| إلى| خَرَجوا| ثُمَّ| مُرَتَّبَةٍ،| صُفوفٍ| في| الطُّلابُ| وَقَفَ|
|stem+| مسرور+ين| ال+مدرسة| الى| ال+طلاب| عاد| ال+ماء| س+قو+ها| ثم| ال+غراس| زرع+وا| ال+ارض| ال+طلاب| حفر| ال+خوخ| ال+ت+ين| غراس| معهم| اخذ+وا| قريب| حقل| الى |خرج+وا| ثم| مرتبة| صفوف| في| ال+طلاب| و+قف|
|stem| مسرور| مدرسة| الى| طلاب| عاد| ماء| قو| ثم| غراس| زرع| ارض| طلاب| حفر| خوخ| تين| غراس| معهم| اخذ| قريب| حقل| الى| خرج| ثم| مرتبة| صفوف| في| طلاب| قف|
|root| سرر| درس| الى| طلب| عاد| ماء| سقو| ثم| غرس| زرع| ارض| طلب| حفر| خوخ| تين| غرس| معهم| اخذ| قرب| حقل| الى| خرج| ثم| رتب| صفف| في| طلب| وقف|

<br>

## How it works

As you can see, the *stemming* gives less accuracy as it's just based on removing affixes (prefixes & suffixes).
<br>
On the other hand, *rooting/lemmatization* gives better accuracy as it works in the background based upon the Taf3eela-تفعيلة system in the Arabic language.


<br>

## Contributors

* Omar AbdulRahman [@omarr45](https://github.com/omarr45)
* Ahmed Tawfik [@fine-simple](https://github.com/fine-simple)
