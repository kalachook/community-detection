/*-******************************************
*  Rahil Sharma                             *
*  Multi-thread Label Propogation Algorithm *
*  (Main Class LP)                          *
*  Modified version                         *
*  Scalable to Multicore Architcture        *
*  Date : 18th October, 2014 (version 1.0)  *
*********************************************/


import javafx.util.Pair;

import java.io.*;
import java.nio.charset.Charset;
import java.util.*;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;


/*-****************************** main class *****************************/
/* Read input file, write output file, Community Detection Algorithm     */
/*-***********************************************************************/

public class Lpni_1 {
    Vector<Node> node_list;
    Vector<Integer> ordered_nodes;
    Vector<Node> node_list1;

    public Lpni_1() { //default constructor
    }

    public static String getEdgeId(int v1, int v2)
    {
        if(v1<v2)
            return Integer.toString(v1) + "_" + Integer.toString(v2);
        return Integer.toString(v2) + "_" + Integer.toString(v1);
    }

    public void readInput(int total_nodes, String input_file) throws IOException {
        FileReader input = new FileReader(input_file);
        BufferedReader br = new BufferedReader(input);
        node_list = new Vector<Node>(total_nodes);
        node_list1= new Vector<Node>(total_nodes);
        ordered_nodes = new Vector<Integer>(total_nodes);

        for (int i = 0; i < total_nodes; i++) {
            node_list.add(new Node(i, i));                       //adding all the nodes to the node list
            ordered_nodes.add(i);                                 //Preserving order of nodes
        }

        System.out.println(total_nodes + " nodes added.");
       // System.out.println("Line  is "+node_list);
        String input_lines = br.readLine();

        while (input_lines!=null  && !input_lines.isEmpty()    ) {
            //System.out.println("Line  is "+input_lines);
            String[] split = input_lines.split(" ");
            //System.out.println(split[0]+" "+split[1]+"\n");
            int v1 = Integer.valueOf(split[0]);
            int dfreq = Integer.valueOf(split[1]);
            node_list.get(v1).df = dfreq;
            input_lines = br.readLine();
        }
         
        input_lines = br.readLine();

        while(input_lines!=null && !input_lines.isEmpty()) {
            String[] split = input_lines.split(" ");        //spliting each lines by spaces
            //System.out.println(split[0]+split[1]+split[2]);
            int v1 = Integer.valueOf(split[0]);            //first half be node v1
            int v2 = Integer.valueOf(split[1]);            //second half be node v2
            int wt = Integer.valueOf(split[2]);           //edge weight
            node_list.get(v1).append_neighbors(v2);        //add v2 in the neighborlist of v1
            node_list.get(v2).append_neighbors(v1);        //add v1 in the neighborlist of v2
            node_list.get(v1).getEdgesWeight().put(getEdgeId(v1, v2), wt);
            node_list.get(v2).getEdgesWeight().put(getEdgeId(v2, v1), wt);
            input_lines = br.readLine();                    //next line
        }

        br.close();
    }

 

/*-************************** Write output file ***************************-*/
/*                       Format : "node_id community label"                 */
/*-************************************************************************-*/

    public void final_communities(String file) throws IOException {
        Map<Integer, Integer> assign_label = new HashMap<Integer, Integer>();
        int label_count = 0;
        for (int i = 0; i < node_list.size(); i++) {
            int label = node_list.get(i).get_label_name();
            Integer r = assign_label.get(Integer.valueOf(label));
            if (r == null) {
                label_count++;
                assign_label.put(Integer.valueOf(label), Integer.valueOf(label_count));
            }
        }
        System.out.println("No of communities = " + label_count);
/* label_count communities found */
        FileOutputStream fso = new FileOutputStream(file);
        OutputStreamWriter fileWriter = new OutputStreamWriter(fso, Charset.forName("UTF-8"));
        Node node;
        for (int i = 0; i < node_list.size(); i++) {
            node = node_list.get(i);
            fileWriter.write(node.get_id() + "--" + assign_label.get(Integer.valueOf(node.get_label_name())).intValue() + "\n");
        }
        System.out.println("DONE");
        fileWriter.close();
        fso.close();
     //  System.out.println("Line  is "+node_list);
    }


/*-************************** Community Detection ***********************-*/
/*Multi-Threading can also be adapted to multi-processor architecture     */
/*-**********************************************************************-*/

    public void communityDetection(int total_threads) throws IOException, ExecutionException, InterruptedException {

        ExecutorService threadPool = Executors.newFixedThreadPool(total_threads);
        Vector<FindDominantLabel> dominantLabel_Calc = new Vector<FindDominantLabel>(total_threads);
        for (int i = 0; i < total_threads; i++) {
            dominantLabel_Calc.add(new FindDominantLabel(node_list));
        }

        //int iteration = 0;
        int label_change = 100; //number of nodes change labels (unstable configuration)
        while (label_change > 0) {

            label_change = 0;
            Collections.shuffle(ordered_nodes);

            //PARALLELISM
            for (int i = 0; i < node_list.size(); i += total_threads) {    //for all nodes

                for (int j = 0; j < total_threads; j++) {                   //blocks of total threads number of nodes run parallel together
                    if ((i + j) < node_list.size())                            // if there are enough nodes(= number of threads) to run parallely
           /*pull each of the j threads from vector (dominantLabel_Calc) and link
             each node from the ordered list to a thread (one to one mapping) */
                        dominantLabel_Calc.get(j).link_node_to_process(ordered_nodes.get(i + j).intValue());
                    else
                        dominantLabel_Calc.get(j).link_node_to_process(-1);
                }

                List<Future<Boolean>> result = threadPool.invokeAll(dominantLabel_Calc);
                for (int k = 0; k < result.size(); k++) {
                    Boolean b = result.get(k).get();
                    if (b != null && b.booleanValue() == true) {
                        label_change++;
                        if (label_change == 1)
                             //System.out.print("once more");
                            break;
                    }
                }

            }

        }

        System.out.println("Communities found");
        threadPool.shutdown();
    }

    public class SortDesc implements Comparator<Pair<Integer, Integer>>
    {
        @Override
        public int compare(Pair<Integer, Integer> o1, Pair<Integer, Integer> o2) {
            return o2.getValue() - o1.getValue();
        }
    }
     public class SortAesc implements Comparator<Pair<Integer, Integer>>
    {
        @Override
        public int compare(Pair<Integer, Integer> o1, Pair<Integer, Integer> o2) {
            return o1.getValue() - o2.getValue();
        }
    }

    public void communityLpni(int maxIter)
    {
        int iteration = 0;
        int lflag = 1;
        int i;
        int j;
        Node currNode;
        Node currNode1;
        Node currNode2;
        int nodeNum;
        int nodeNum2;
        int k=0;
        
       

        ArrayList<Pair<Integer,Integer>> orderSeq = new ArrayList<Pair<Integer, Integer>>();
         ArrayList<Pair<Integer,Integer>> orderSeq1 = new ArrayList<Pair<Integer, Integer>>();
        // ArrayList<Pair<Integer,Integer>> orderSeq2 = new ArrayList<Pair<Integer, Integer>>();
         List<Integer> nodeseq = new ArrayList<Integer>();
         // ArrayList<Integer> orderSeq = new ArrayList<Integer>();
           
        ArrayList<Integer> l1 = new ArrayList<Integer>();
       
        for(i=0;i<node_list.size();i++)
        {
            int sum=0;
            currNode = node_list.get(i);
            
            //orderSeq.add(new Pair<Integer,Integer>(i,currNode.get_neighbors().size()));
          orderSeq.add(new Pair<Integer,Integer>(i,currNode.df));
            // orderSeq.add(new Pair<Integer,Integer>(i,sum));
        }
        Collections.sort(orderSeq, new SortDesc());
        //System.out.println("Distinct List "+node_list);
        // node_list.clear();
         //ordered_nodes.clear();
       for(Pair<Integer, Integer> p2: orderSeq)
              {
                nodeNum2 = p2.getKey();
               // int index = node_list.indexOf(nodeNum2);
                

                 currNode1 = node_list.get(nodeNum2);
                     for( Integer neighborId: currNode1.get_neighbors())
                        {
                            //int index1 = node_list.indexOf(currNode2);
                           // orderSeq1.add(new Pair<Integer,Integer>(neighborId,node_list.get(neighborId).df));
                            //  orderSeq1.add(new Pair<Integer,Integer>(neighborId,currNode1.get_neighbors().size()));
                               orderSeq1.add(new Pair<Integer,Integer>(neighborId,node_list.get(neighborId).getEdgesWeight().get(getEdgeId(neighborId,nodeNum2))));
                            //  orderSeq1.add(new Pair <Integer, Integer> (neighborId,(int)(node_list.get(neighborId).getEdgesWeight().get(getEdgeId(neighborId,nodeNum2))/(node_list.get(neighborId).df * 1.00)*100000)));
                        } 
                     Collections.sort(orderSeq1, new SortAesc());
                   //  System.out.println(nodeNum2);
                    // System.out.println(orderSeq1);
                     for(Pair<Integer, Integer> p1: orderSeq1)
                        {
                             nodeNum = p1.getKey();
                             if (nodeseq.contains(nodeNum)==false) 
                                  nodeseq.add(nodeNum);
                         }
                     if(nodeseq.contains(nodeNum2)==false)
                        nodeseq.add(nodeNum2);    
                        orderSeq1.clear();
           }
          
      //   System.out.print("nodelist" +nodeseq);
          int nodeNum1;
        int ans;
       // System.out.println(nodeseq);
        DominantLabel dl = new DominantLabel(node_list);
            
          while (iteration<maxIter && lflag>0)
        {
            lflag = 0;
           // System.out.println("Iteration " + iteration + "\n" + "nodeNum");
            for(int demo=0;demo<nodeseq.size();demo++)
            {
                nodeNum1 = nodeseq.get(demo);
               // System.out.print(nodeNum + " ");
                ans = dl.updateLabel(nodeNum1);
                if(lflag==0 && ans==1)
                    lflag=1;
            }
            //System.out.println("\n");
            iteration++;
        }

            
       
        
          
         

    }

/*-************************** Main***************************************-*/
/*Change number of threads here, (also othe r parameters)                  */
/*-**********************************************************************-*/


    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {
        Lpni_1 algo = new Lpni_1();
        //to know how many nodes there
        int count=0;
        File demoFile = new File("sample_input.txt");
        Scanner sc = new Scanner(demoFile);
        while(sc.hasNextLine()){
            count++;
            if(sc.nextLine().equals(""))
                break;
            // System.out.println(sc.nextLine());
        }    
        int total_nodes = count-1;                        // Total nodes in the input graph

        algo.readInput(total_nodes, "sample_input.txt");

        long startTime = System.currentTimeMillis();

        algo.communityLpni(1000000000);

        long endTime = System.currentTimeMillis();
        long totalTime = endTime - startTime;

        System.out.println("Time_Taken " + totalTime / 1000.0);
        algo.final_communities("ans1.txt");
      }

 }
