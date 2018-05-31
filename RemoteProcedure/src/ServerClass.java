import java.rmi.AlreadyBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class ServerClass {


    public ServerClass(){
    }

    public static void main(String [] args){

        try {
            // Instantiating the implementation class
            Greet obj = new Greet();

            // Exporting the object of implementation class
            // (here we are exporting the remote object to the stub)
            PrintMessage stub = (PrintMessage) UnicastRemoteObject.exportObject(obj, 0);

            // Binding the remote object (stub) in the registry
            Registry registry = LocateRegistry.getRegistry();

            registry.bind("Hello", stub);
            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }

}

}
