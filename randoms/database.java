import java.util.*;
public class database {
    int count = 0;
    List <String> tasks = new ArrayList<String>();

    public void kanish(String task)
    {
        try{
            tasks.add(task);
            count++;
        } catch(Exception e) {
            System.out.println("something went wrong");
        }
        
    }

    public void remove(String task)
    {
        try
        {
            if (tasks.contains(task))
            {
            tasks.remove(task);
            count--;
            } else{
                System.out.println("Task not present");
            }
            
        } catch (Exception e) {
            System.out.println("task not present");
        }
    }

    public void display()
    {
        System.out.println("tasks present:");
        System.out.println(tasks);
        System.out.println(String.format("Total tasks remaining are: %d",count));
    }
}
