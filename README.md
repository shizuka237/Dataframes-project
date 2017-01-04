# Dataframes-project
For integrating data from multiple sources
Following and are input/output scenarios of my program , inputs are marked in bold:

Example 1 : Combining CSV and MySQL objects
Enter no of DataSources you want to join/ Enter tweet in case of twitter 

2

Enter the type(csv /sql) , (tablename/filename) , (fields)  in following 2 lines

sql,CUSTOMERS,CustomerID,City

SELECT CustomerID, City  FROM CUSTOMERS

  CustomerID         City

0      ALFKI       Berlin

1      ANATR  México D.F.

2      ANTON  México D.F.

3      AROUT       London

4      BERGS        Luleå

-----------------------------------------------

csv,orders.csv,CustomerID,OrderID

  CustomerID  OrderID

0      VINET    10248

1      TOMSP    10249

2      HANAR    10250

3      VICTE    10251

4      SUPRD    10252

-----------------------------------------------

Enter Join Field names (separated by Commas)

CustomerID

-----Joining------s

['CustomerID']

  CustomerID    City  OrderID

0      ALFKI  Berlin  10643.0

1      ALFKI  Berlin  10692.0

2      ALFKI  Berlin  10702.0

3      ALFKI  Berlin  10835.0

4      ALFKI  Berlin  10952.0

"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

Example 2 : Using Twitter API



Enter no of DataSources you want to join/ Enter tweet in case of twitter 

twitter

enter the topic name to mine tweets on

iphone

            u_id                  Name       ScreenName  \

0   1.474996e+09         SellusDomains    Sellusdomains   

1   2.722281e+09       ✨Hattypie ✨🎅🏻         hattypie   

2   5.295112e+08                bim ⚡️        kimontiv_   

3   1.312517e+09       Sterling Archer       Archer0015   

4   7.192063e+17       Tech News Daily   technewsbuzzer   

5   2.911556e+08               (a)lena      jesuisaleee   

6   2.789492e+09         Dika Fernando         dikamian   

7   1.166136e+08                    B.  SheIsABlessing_   

8   2.245508e+09  Young Fiji Water🌙💦  MumboSauceWalka   

9   7.247319e+17           Demetric 🐂    Lightskinmerc   

10  4.644626e+09     GenesisRealEstate    TeamGenesisRE   

11  2.224054e+08           bruce rosga  alaskanpolarcat   

12  1.964071e+09           muzelloader       Alvin_Lear   

13  3.321593e+08                munish    munishJagbani   

14  5.248168e+08      Victor Strömgren   VictorStrmgren   

15  1.188035e+08    Retired Villian 🤔  Des_Awesome_Iam   



                                                 text  

0   RT @CommercialNames: Download Double Up Seven’...  

1   @Sharleenflry oh no ! I really hate that. 😪 M...  

2   I was getting tired of my bf playing 8 ball on...  

3   I'm loving Cercube for YouTube on my iPhone! h...  

4   The Week in iPhone and iPad Cases: Bring home ...  

5   that's my iPhone\n....1 year ago https://t.co/...  

6   The Week in iPhone and iPad Cases: Bring home ...  

7   RT @YouTuberProbs_: iPhone: would you like to ...  

8   Y'all really wasted a iPhone by putting trumps...  

9   I'll sit right next to the charger and won't u...  

10  The real estate Daily is out! https://t.co/iUI...  

11  RT @KellyannePolls: Grateful &amp; humble, @re...  

12  RT @KellyannePolls: Grateful &amp; humble, @re...  

13  https://t.co/DEVH2JdnW5\nAPPLE IPHONE FOR SALE...  

14  RT @iTem70: Just because of the tremendous pri...  

15                              IPhone games anyone??  

--implimenting word count---

Sunnys-MacBook-Air:smritiRaj sunny$ python tester.py 

Enter no of DataSources you want to join/ Enter tweet in case of twitter 

twitter

enter the topic name to mine tweets on

iphone

            u_id                  Name       ScreenName  \

0   2.261768e+09       LaurenGwendolyn  LaurenGwendolyn   

1   2.494943e+09         LowmanMarlowe    LowmanMarlowe   

2   1.593725e+09             Guwopmole          depic45   

3   7.075661e+17       BaconImpossible     VentureBacon   

4   1.396100e+09                   Car          C_Los05   

5   7.958514e+17            #Happy1111      happy1111us   

6   1.651355e+08             Joc (5-9)      jocelyn3328   

7   2.376561e+09                 Maria    Maria_Bt11800   

8   2.711898e+08               Madison        Madisonnl   

9   1.131676e+09                 baka.       foxcorpses   

10  7.610604e+17                  Ty⛓⚔        wessideTy   

11  1.413939e+09   @QuiteTheCharacter_        Yanalynn_   

12  5.786135e+08  Serge L. (Vet.) 🇺🇸       Cubannator   

13  4.225209e+09                  Rias  perfectionjimin   

14  3.004013e+09   SendHolesToYourFoes       PaperHoles   

15  2.509775e+08              March 30     PrettiiKayla   



                                                 text  

0   Twitter down_ site stops working as it refuses...  

1   Twitter down_ site stops working as it refuses...  

2   Only annoying thing bout the iPhone 7 being wa...  

3   RT @CommercialNames: Download Double Up Seven’...  

4     Someone buy me an iphone armband for when i run  

5   #iphone #free #style #newdeals #music #usb #ch...  

6   RT @TravusHertl: Imagine carrying a child in y...  

7   @jaramjes009 lmao jess if I could I'd buy you ...  

8   trying to get my iPhone 4 to turn on just so i...  

9   RT @mitchwelling: i was setting up a new touch...  

10  RT @Too_Luxury: His teacher took his Iphone so...  

11  RT @American_Angel8: WIM GOT AN IPHONE! Lmao I...  

12  .@Apple has been asked to help unlock Mevlut M...  

13  RT @Ahzure_: Giving 15 iPhone 7's to 15 lucky ...  

14  RT @CommercialNames: Download Double Up Seven’...  

15  I'm now an E-List celebrity in Kim Kardashian:...  

--implimenting word count---

            u_id                  Name       ScreenName  \

0   2.261768e+09       LaurenGwendolyn  LaurenGwendolyn   

1   2.494943e+09         LowmanMarlowe    LowmanMarlowe   

2   1.593725e+09             Guwopmole          depic45   

3   7.075661e+17       BaconImpossible     VentureBacon   

4   1.396100e+09                   Car          C_Los05   

5   7.958514e+17            #Happy1111      happy1111us   

6   1.651355e+08             Joc (5-9)      jocelyn3328   

7   2.376561e+09                 Maria    Maria_Bt11800   

8   2.711898e+08               Madison        Madisonnl   

9   1.131676e+09                 baka.       foxcorpses   

10  7.610604e+17                  Ty⛓⚔        wessideTy   

11  1.413939e+09   @QuiteTheCharacter_        Yanalynn_   

12  5.786135e+08  Serge L. (Vet.) 🇺🇸       Cubannator   

13  4.225209e+09                  Rias  perfectionjimin   

14  3.004013e+09   SendHolesToYourFoes       PaperHoles   

15  2.509775e+08              March 30     PrettiiKayla   



                                                 text  uniqueWords  

0   Twitter down_ site stops working as it refuses...           24  

1   Twitter down_ site stops working as it refuses...           20  

2   Only annoying thing bout the iPhone 7 being wa...           20  

3   RT @CommercialNames: Download Double Up Seven’...           19  

4     Someone buy me an iphone armband for when i run           10  

5   #iphone #free #style #newdeals #music #usb #ch...           13  

6   RT @TravusHertl: Imagine carrying a child in y...           23  

7   @jaramjes009 lmao jess if I could I'd buy you ...           12  

8   trying to get my iPhone 4 to turn on just so i...           15  

9   RT @mitchwelling: i was setting up a new touch...           23  

10  RT @Too_Luxury: His teacher took his Iphone so...           13  

11  RT @American_Angel8: WIM GOT AN IPHONE! Lmao I...           22  

12  .@Apple has been asked to help unlock Mevlut M...           14  

13  RT @Ahzure_: Giving 15 iPhone 7's to 15 lucky ...           24  

14  RT @CommercialNames: Download Double Up Seven’...           19  


15  I'm now an E-List celebrity in Kim Kardashian:...           19  