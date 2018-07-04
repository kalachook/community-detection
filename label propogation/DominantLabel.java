import java.util.Vector;

/**
 * Created by mitta on 02-Jan-18.
 */
public class DominantLabel {

    public Vector<Node> nodeList;

    private Vector<Integer> dominantLabels = new Vector<Integer>();
    private Vector<Integer> labelCount;
    private Vector<Double> labelValue;

    public DominantLabel(Vector<Node> nodeList)
    {
        this.nodeList = nodeList;
        labelCount = new Vector<Integer>(nodeList.size());
        labelValue = new Vector<Double>(nodeList.size());
    }

    public int updateLabel(int nodeId)
    {
        int i;
        int flag=1;

        dominantLabels.clear();
        labelCount.clear();
        labelValue.clear();

        for(i=0;i<nodeList.size();i++)
        {
            labelCount.add(Integer.valueOf(0));
            labelValue.add(Double.valueOf(0));
        }


        int maxCount = 0;
        Node currNode = nodeList.get(nodeId);

        for(Integer neighborId: currNode.get_neighbors())
        {
            double sum=0;
            int sum1=0;
            int sum2=0;
            int neighborLabel = nodeList.get(neighborId).get_label_name();
            int neighborLabelCount = labelCount.get(neighborLabel) + 1;
            for(Integer neighborIdChild : nodeList.get(neighborId).get_neighbors())
              { 
                 for(Integer neighborIdChild1 : nodeList.get(neighborIdChild).get_neighbors())
                    {
                       sum2 = sum2 + nodeList.get(neighborIdChild1).getEdgesWeight().get(Lpni.getEdgeId(neighborIdChild1, neighborIdChild));
                    }
                
               sum1 = sum1 + nodeList.get(neighborIdChild).getEdgesWeight().get(Lpni.getEdgeId(neighborIdChild, neighborId));
                sum = sum + (nodeList.get(neighborIdChild).df/nodeList.get(neighborIdChild).get_neighbors().size());
                 // sum = sum + (nodeList.get(neighborIdChild).get_neighbors().size()/sum2);
              }
            // double neighborLabelWeight = labelValue.get(neighborLabel) + ((sum+nodeList.get(neighborId).df) * (nodeList.get(nodeId).getEdgesWeight().get(Lpni.getEdgeId(nodeId,neighborId)))/nodeList.get(neighborId).get_neighbors().size());
           // double neighborLabelWeight = labelValue.get(neighborLabel) + ((sum+nodeList.get(neighborId).df)/(nodeList.get(neighborId).get_neighbors().size()));
           // double neighborLabelWeight = labelValue.get(neighborLabel) + (sum+nodeList.get(neighborId).df);
           //  double neighborLabelWeight = labelValue.get(neighborLabel) + ((sum+nodeList.get(neighborId).df)/sum1);
           double neighborLabelWeight = labelValue.get(neighborLabel) + (sum1/nodeList.get(neighborId).get_neighbors().size());
            // double neighborLabelWeight = labelValue.get(neighborLabel) + (sum/nodeList.get(neighborId).get_neighbors().size());
          // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0 * currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId)))/(nodeList.get(neighborId).get_neighbors().size());
           //  double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0 * currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId))/(sum));
           // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0/(sum));
            // double neighborLabelWeight = labelValue.get(neighborLabel) + ((currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId)))/(nodeList.get(neighborId).get_neighbors().size()));
           // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).get_neighbors().size());
          // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0);
        // double neighborLabelWeight = labelValue.get(neighborLabel) + ((currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId)))/(nodeList.get(neighborId).df * 1.0));
              // double neighborLabelWeight = labelValue.get(neighborLabel) + (sum2/(currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId)) * 1.0));
          // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0);
          //  double neighborLabelWeight = labelValue.get(neighborLabel) + nodeList.get(nodeId).getEdgesWeight().get(Lpni.getEdgeId(nodeId,neighborId))/(nodeList.get(neighborId).df * 1.0);
         //   double neighborLabelWeight = labelValue.get(neighborLabel) + nodeList.get(nodeId).getEdgesWeight().get(Lpni.getEdgeId(nodeId,neighborId));
            // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0)/(nodeList.get(neighborId).get_neighbors().size());
          //  double neighborLabelWeight = labelValue.get(neighborLabel) + (currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId)));
            // double neighborLabelWeight = labelValue.get(neighborLabel) + (nodeList.get(neighborId).df * 1.0)/(currNode.getEdgesWeight().get(Lpni.getEdgeId(nodeId, neighborId)));

                    //labelValue.get(neighborLabel) + ;

            labelCount.set(neighborLabel, neighborLabelCount);
            labelValue.set(neighborLabel, neighborLabelWeight);

            if(maxCount<neighborLabelCount)
            {
                maxCount = neighborLabelCount;
                dominantLabels.clear();
                dominantLabels.add(neighborLabel);
            }
            else if(maxCount==neighborLabelCount)
            {
                dominantLabels.add(neighborLabel);
            }

        }

        double maxi = 0;
        int choosenLabel = 0;
        for(Integer val: dominantLabels)
        {
            if(maxi< labelValue.get(val))
            {
                maxi = labelValue.get(val);
                choosenLabel = val;
            }
        }

        if(dominantLabels.contains(Integer.valueOf(currNode.get_label_name())) && labelValue.get(currNode.get_label_name())==maxi)
        {
            flag=0;
        }
        else
        {
            currNode.set_label_name(choosenLabel);
        }

        return flag;
    }

}
