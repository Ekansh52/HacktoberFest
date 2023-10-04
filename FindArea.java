import java.util.*;
class RectangleShape
{
   int length, breadth;
   // rectangle constructor java
   RectangleShape(int l, int b) 
   { 
      length = l; 
      breadth = b; 
   } 
   RectangleShape(int l) 
   { 
      length = l; 
      breadth = 20; 
   } 
   RectangleShape() 
   { 
      length = 6; 
      breadth = 2; 
   } 
   float getArea() 
   { 
      return(length * breadth); 
   }
}
public class FindArea 
{
   public static void main(String[] args)
   {
      RectangleShape rs1 = new RectangleShape(); 
      RectangleShape rs2 = new RectangleShape(60); 
      RectangleShape rs3 = new RectangleShape(40, 20); 
      System.out.println("First rectangle : " + rs1.getArea()); 
      System.out.println("Second rectangle : " + rs2.getArea()); 
      System.out.println("Third Rectangle : " + rs3.getArea());
   }
}