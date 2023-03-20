class arjun
{
    public static void main(String []args)
    {
        database myobj = new database();

        myobj.kanish("eating");
        myobj.remove("project");
        myobj.display();
    } 



    public static int factorial(int num)
    {
        int fact = 1;

        for(int i =1 ; i <= num ; i++)
        {
            fact = fact * i;
        }
        return fact;
    }
    
}
