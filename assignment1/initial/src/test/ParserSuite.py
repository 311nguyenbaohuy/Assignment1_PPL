import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
 
    def test1(self):
        input = """
        void main(){
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test2(self):
        input = """
        int main;
        main = 1;
        void main(){
            return main;
        }"""
        expect = "Error on line 3 col 8: main"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test3(self):
        input = """
        int main[3];
        void main(){
            a[foo(a[a])] = foo;
            return main;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test4(self):
        input = """void main( ){ if (a) if (b) if (c) a; else a; else }"""
        expect = "Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test5(self):
        input = """
        float a;
        boolean b;
        string a[0];
        
        float main(){
            a = 1;
            b = false;
            b = true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test6(self):
        input = """
        void main(){ 
            int a; 
            a = "avc" 
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test7(self):
        input = """
        void main(){ 
            a = ((a[b] || 1) % 2 ); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test8(self):
        input = """
        string main(){
            // comment 
            /* @author:
        }
        """
        expect = "@"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test9(self):
        input = """
        int a[000];
        string main(){
            // comment 
            /* @author: 
            */
            a = ((1+2) / 3) * a[1-(1+2)*3];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test10(self):
        input = """
        int[] a {
            for(i=1;i<2<3;i/2){
                return 1;
            }
        }
        string main(){
            a = ((1+2) / 3) * a[1-(1+2)*3];
        }
        """
        expect = "Error on line 2 col 16: {"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test11(self):
        input = """
        int[] a() {
            for(i=1;i<2<3;i/2){
                return 1;
            }
        }
        string main(){
            a = ((1+2) / 3) * a[1-(1+2)*3];
        }
        """
        expect = "Error on line 3 col 23: <"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test12(self):
        input = """
        string main(){
            a = ((1+2) / 3) * foo(a[1-(1+2)*3]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test13(self):
        input = """
        string main(){
            a = ((1+2) / 3) * foo(a[1-(1+2)*3]);
            return;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test14(self):
        input = """
        void foo() {
            int a; 
            a = 1;
            return a;
        }
        string main(){
            return;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))


    def test15(self):
        input = """
        string main(){
            a = ((1+2) / 3) * foo(a[1-(1+2)*3]);
            return a
        }
        """
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test16(self):
        input = """
        string main(){
            a = ((1+2) / 3) * foo(a[1-(1+2)*3]);
            return a;;
        }
        """
        expect = "Error on line 4 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test17(self):
        input = """
        string main(){
            a(1) = (((((2)))));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    def test18(self):
        input = """
        
        """
        expect ="Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,218)) 

    def test19(self):
        input = """
        int main{
            println("Hello world");
        }
        """
        expect ="Error on line 2 col 16: {"
        self.assertTrue(TestParser.checkParser(input,expect,219)) 

    def test20(self):
        input = """
        void main(){
            for (a<1; b <2; )
                i+1;
        }
        """
        expect ="Error on line 3 col 28: )"
        self.assertTrue(TestParser.checkParser(input,expect,220)) 

    def test21(self):
        input = """
        void main(){
            for (a < 1; b = 1; c-1){
                int i;
            }
            {
                i =2;
            }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,221)) 

    def test22(self):
        input = """
        void main(){
            foo(a[1], (b/2)*(4+3)) = (a)[2];
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,222)) 
    
    def test23(self):
        input = """
        boolean main(){
            a[2][2] = true;
        }
        """
        expect ="Error on line 3 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,223)) 
    
    def test24(self):
        input = """
        boolean main(){
            ((a[2])[2])[2] = 3;
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,224)) 

    def test25(self):
        input = """
        int a = 1;
        """
        expect ="Error on line 2 col 14: ="
        self.assertTrue(TestParser.checkParser(input,expect,225)) 

    def test26(self):
        input = """
        int a[]
        """
        expect ="Error on line 2 col 14: ]"
        self.assertTrue(TestParser.checkParser(input,expect,226)) 
        
    def test27(self):
        input = """
        int a[]
        """
        expect ="Error on line 2 col 14: ]"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test28(self):
        input = """
        int a[1], b, c; 
        int foo(int a, int b[]){
            int func (){

            }
        }
        """
        expect ="Error on line 4 col 21: ("
        self.assertTrue(TestParser.checkParser(input,expect,228)) 
         
    def test29(self):
        input = """
        int a[1], b, c; 
        int main(){
            a < b<c;   
        }
        }
        """
        expect ="Error on line 4 col 17: <"
        self.assertTrue(TestParser.checkParser(input,expect,229)) 
         
    def test30(self):
        input = """
        int a[1], b, c; 
        int main(){
            a == b == c;   
        }
        }
        """
        expect ="Error on line 4 col 19: =="
        self.assertTrue(TestParser.checkParser(input,expect,230)) 
         
    def test31(self):
        input = """
        int a[1], b, c; 
        int main(){
               a = ((a - b) * c || e1 - b )|| d * c;   
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,231)) 
         
    def test32(self):
        input = """
        int a[1], b, c; 
        int main(){
            a = 10; // OK   
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,232)) 
    
    def test33(self):
        input = """
        int a[1], b, c; 
        int main(){
            if ( a || 1)
                if (b)
                    {

                    }
                    {

                    }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,233)) 
    
    def test33(self):
        input = """
        int a[1], b, c; 
        int main(){
            if ( a || 1)
                if (b)
                    {

                    }
                    {

                    }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,233)) 
    
    def test34(self):
        input = """
        int a[1], b, c; 
        int main(){
            if ( a || 1)
                if (b)
                    {

                    }
                    {

                    }
                else
                    1;
        }
        """
        expect ="Error on line 12 col 16: else"
        self.assertTrue(TestParser.checkParser(input,expect,234)) 
    
    def test35(self):
        input = """
        int a[1], b, c; 
        int main(){
            if ( a || 1)
                if (b)
                    {
                        {  
                        }
                    }
                    
                else
                    1;
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,235)) 
    
    def test36(self):
        input = """
        int a[1], b, c; 
        int main(){
            if ( a || 1)
                do {
                    a;
                }
                { }
                while (1);
            else{ }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,236)) 
    
    def test37(self):
        input = """
        int a[1], b, c; 
        int main(){
            for (true; false; true){
                true;
            }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,237)) 
    
    def test38(self):
        input = """
        int a[1], b, c; 
        int main(){
            for (true; false; true){
                break;
            }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,238)) 

    def test39(self):
        input = """
        int a[1], b, c; 
        int main(){
            for (true; false; true){
                continue;
            }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,239)) 
    
    def test40(self):
        input = """
        int a[1], b, c; 
        int main(){
            a == b == c != d;
        }
        """
        expect ="Error on line 4 col 19: =="
        self.assertTrue(TestParser.checkParser(input,expect,240)) 
    
    def test41(self):
        input = """
        int a[1], b, c; 
        int main(){
            for (1.31e-1; 00.e1; 1.e){
                continue;
            }
        }
        """
        expect ="Error on line 4 col 35: e"
        self.assertTrue(TestParser.checkParser(input,expect,241)) 
    
    def test42(self):
        input = """
        int for (){

        }
        int main(){ }
        """
        expect ="Error on line 2 col 12: for"
        self.assertTrue(TestParser.checkParser(input,expect,242)) 
    
    def test43(self):
        input = """
        int main(){ 
            for (i; i < 10; foo(2)[1+x*(1/2)]/3)
                {}{} break;
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,243)) 

    def test44(self):
        input = """
        int main(){ 
            for (i; i < 10; foo(2)[1+x*(1/2)]/3)
                if (a){{}a;{}}
                else {b;}
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,244)) 
    
    def test45(self):
        input = """
        int main(){ 
            foo(_,_,1.e1,2);
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,245)) 
    
    def test46(self):
        input = """
        int main(){ 
            a[2] = a[4] = a[5] = a[a] == a; 
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,246)) 
    
    def test47(self):
        input = """
        int[] foo(int a[1], 2){} 
        
        int main(){ 
            foo(_,_,1.e1,2);
        }
        """
        expect ="Error on line 2 col 24: 1"
        self.assertTrue(TestParser.checkParser(input,expect,247)) 
    
    def test48(self):
        input = """
        int main(){ 
            a =  // abc
        }
        """
        expect ="Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,248)) 

    def test49(self):
        input = """
        int main(){ 
            if (a > b) return;
            return void;
        }
        """
        expect ="Error on line 4 col 19: void"
        self.assertTrue(TestParser.checkParser(input,expect,249)) 
    
    def test50(self):
        input = """
        int main(){ 
            if (1) printf("%d", c);
            else print("d");
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,250)) 
    
    def test51(self):
        input = """
        int main(){ 
            if (a != 1){
                {
                    if (a = 1){
                        { }
                    }
                    else a;
                }
            }
            else { //if }
            }
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,251)) 
    
    def test52(self):
        input = """
        int main(){ 
            for (int i; i < 10; 10){

            }
        }
        """
        expect ="Error on line 3 col 17: int"

        self.assertTrue(TestParser.checkParser(input,expect,252)) 
    
    def test53(self):
        input = """
        int main(){ 
            for (1.3;1;"e")
                do{
                }
                {}
                while(1);
        }
        """
        expect ="successful"

        self.assertTrue(TestParser.checkParser(input,expect,253)) 
    
    def test54(self):
        input = """
        int main(){ 
            do
                int a;
            while(1);
        }
        """
        expect ="Error on line 4 col 16: int"

        self.assertTrue(TestParser.checkParser(input,expect,254)) 
    
    def test55(self):
        input = """
        void string (){
            return "1";
        }
        """
        expect ="Error on line 2 col 13: string"

        self.assertTrue(TestParser.checkParser(input,expect,255)) 
    
    def test56(self):
        input = """
        void main (){
            for (i; 1; fasle){
                "abc"[1] = 1;
            }
        }
        """
        expect ="successful"

        self.assertTrue(TestParser.checkParser(input,expect,256)) 
    
    def test57(self):
        input = """
        int a (){
            do {{(1)}{(1)}}
            while(1);
        }
        }
        """
        expect ="Error on line 3 col 20: }"
        self.assertTrue(TestParser.checkParser(input,expect,257)) 
    
    def test58(self):
        input = """
        int void[8];
        """
        expect = "Error on line 2 col 12: void"
        self.assertTrue(TestParser.checkParser(input,expect,258)) 
    
    def test58(self):
        input = """
        int void[8];
        """
        expect = "Error on line 2 col 12: void"
        self.assertTrue(TestParser.checkParser(input,expect,258)) 

    def test59(self):
        input = """
        int foo(){
            a = ("string"[2])[2];
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259)) 
    
    def test60(self):
        input = """
        int foo(){
            for (1;2;3)
                if (1 > 2){

                }
            { }
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260)) 
    
    def test61(self):
        input = """
        int foo(){
            do 
            break;
            continue();
            while(1);
        }         
        """
        expect = "Error on line 5 col 20: ("
        self.assertTrue(TestParser.checkParser(input,expect,261)) 
    
    def test62(self):
        input = """
        int foo(){
            do 
            while(1);
        }         
        """
        expect = "Error on line 4 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test63(self):
        input = """
        int foo(){
            do
                for ("a"; "b"; "c")
                    retunr;
            while(main);
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test64(self):
        input = """
        int foo(){
            do
                if (main)
                    reutr;
                else
                    reutnr;
            while(main);
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test65(self):
        input = """
        int foo(){
            do
                continue;
            while(main);
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))


    def test66(self):
        input = """
        int foo(){
            do
                break;
            while(main);
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))


    def test67(self):
        input = """
        int foo(){
            i = 1;
            int i;
            {
                i = 1;
            }
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test68(self):
        input = """
        int foo(int a, string b, float c){
            int a [1];
            a[2] = 0;
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test69(self):
        input = """
        int[] foo(int a, string b, float c){
            int a [1.2];
            a[0] = 0;
        }         
        """
        expect = "Error on line 3 col 19: 1.2"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    
    def test70(self):
        input = """
        int[] foo(int a, string b, float c){
        }         
        string [] foo(int a[]){

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test71(self):
        input = """
        void[] main(){

        }
        """
        expect = "Error on line 2 col 12: ["
        self.assertTrue(TestParser.checkParser(input,expect,271))
    
    def test72(self):
        input = """
        void main(){
            a > b == c;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    
    def test73(self):
        input = """
        void main(){
            a > b > "abc";
        }
        """
        expect = "Error on line 3 col 18: >"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test74(self):
        input = """
        void main(){
            a > b <= "abc";
        }
        """
        expect = "Error on line 3 col 18: <="
        self.assertTrue(TestParser.checkParser(input,expect,274))
    
    def test75(self):
        input = """
        void main(){
            a > !"abc";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test76(self):
        input = """
        void main(){
            a / b + (c * d)[a / b];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test77(self):
        input = """
        void main(){
            if (a > b){
                if (b > c){

                }
                else{

                }
            }
            else(12);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test78(self):
        input = """
        void main(){
            int _, b, c;
            _ = 1;
            for (1;1;1){
                do{}{} while(1);
            }
            if(a) for(1;1;1){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test79(self):
        input = """
        void main(){
            if (1.2e1){

            }
            else{
                1;2;3;"abc";1abc1
            }
        }
        """
        expect = "Error on line 7 col 29: abc1"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    
    def test80(self):
        input = """
        void main(){
            a = 1.e0[_abc_] + "abc";
           do{{ if (a>0) a;}} while (a>0);
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test81(self):
        input = """
        {
            int main;
        }
        """
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test82(self):
        input = """
        int main()
        {
            if (a) 
                if (b)
                    if (c)
                        if (d) E;
                    else(c);
                else(d);
            else(a);

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test83(self):
        input = """
        int main()
        {
            if (a) 
                if (b)
                    if (c)
                        if (d) E;
                    else print("a");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    
    def test84(self):
        input = """
        int main()
        {
           do { } { }
           while(a||b + c && c -a); 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    
    def test85(self):
        input = """
        int main()
        {
            a = ((a || b) + (a % d))/ 2 * (a+(b -c)
        }
        """
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    
    def test86(self):
        input = """
        int main()
        {
            for (int i = 0; i < 10; i++){
                print(i);
            }
        }
        """
        expect = "Error on line 4 col 17: int"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    
    def test87(self):
        input = """
        int main(){ }
        int foo(){ }
        void main(){
            int main, string main;
        }
        """
        expect = "Error on line 5 col 22: string"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test88(self):
        input = """
        void main(){
            do
                for (1;1;1){
                    do
                        for (1;1;1){}
                    while(1);
                }
                { }
            while(1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test89(self):
        input = """
        int main(){ }
        int foo(){ }
        void main(){
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    
    def test90(self):
        input = """
        void main(){
            int (a [1])[2];
        }
        """
        expect = "Error on line 3 col 16: ("
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test91(self):
        input = """
        void main(){
            int (a [1])[2];
        }
        """
        expect = "Error on line 3 col 16: ("
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test92(self):
        input = """
        // check a number is prime number
        boolean isPrimeNumber(int num){ }

        void main(){
            int i;
            for (i = 1; i < 10; i = i + 1)
                print (isPrimeNumber(i));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test93(self):
        input = """
        /* this function is used to ... 
         * ...
         */
        string upper (string a){}
        string arrStr [10];

        void main(){
            int i;
            for (i = 1; i < 10; i = i + 1)
                print (upper(arrStr[i]));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test94(self):
        input = """
        void matrix[10];

        void main(){
            int i;
            for (i = 1; i < 10; i = i + 1)
        }
        """
        expect = "Error on line 2 col 19: ["
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test95(self):
        input = """
        void matrix();

        void main(){
            int i;
            for (i = 1; i < 10; i = i + 1)
        }
        
        void matrix(){
            // do something
        }
        """
        expect = "Error on line 2 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    
    def test96(self):
        input = """
        void main(){
            int i;
            if (a > b != c / d && e)
                main();
        }
        
        void main(){
            // do something
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    
    def test97(self):
        input = """
        if (a > 10) {
            print (a);
        }
        """
        expect = "Error on line 2 col 8: if"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    

    def test98(self):
        input = """
        boolean main(){

        }
        if (a > 10) {
            print (a);
        }
        """
        expect = "Error on line 5 col 8: if"
        self.assertTrue(TestParser.checkParser(input,expect,298))


    def test99(self):
        input = """
        boolean main[10];
        void main(){
            do {
                // something
                i = i + 1;
            }
            while (main[i]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test100(self):
        input = """
        void main(){
            do main > 0;
            while (main > 0); 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))