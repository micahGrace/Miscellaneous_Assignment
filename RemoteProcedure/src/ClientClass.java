
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ClientClass {

    public static  void main(String [] args){

        try {
            // Getting the registry
            Registry registry = LocateRegistry.getRegistry(null);

            // Looking up the registry for the remote object
            PrintMessage stub = (PrintMessage) registry.lookup("PrintMessage");

            // Calling the remote method using the obtained object
            stub.printMessage();

            // System.out.println("Remote method invoked");
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }

    }

}
