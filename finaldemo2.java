class FinalDemo
{  public double a=1000;     //obj var a, Scope: public, non-final
   public final double b=4.56;  //obj var b, Scope: public,final 
   public static final int c=10;  //class var named c, Scope: public,final

 public void displayValues()
 {
 final double a = 20.56;   //local variable named 'a' is declared as final
 final int b=23;
 int c= 20;
 System.out.println(a);
 System.out.println(b);
 System.out.println(c);
 System.out.println(this.a);
 System.out.println(this.b);
 System.out.println(FinalDemo.c);
 }   //End of method
}//End of class

class FinalDemoTest
{    
  public static void main (String args[])
  { FinalDemo d1= new FinalDemo();
    d1.displayValues();
  } //End of method
} //End of class



