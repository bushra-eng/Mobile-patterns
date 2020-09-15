
#
#
#
# **********************************************************************************************************************************************



def  count_patterns_from(firstPoint,length):
  graph={'A':['B','D','E','F','H'],'B':['A','D','E','F','C','G','I'],'C':['B','E','F','D','H'],'D':['C','I','A','B','E','H','G'],'E':['A','B','C','D','F','G','H','I'],'F':['B','C','E','H','I','A','G'],'G':['D','E','H','B','F'],'H':['D','E','F','G','I','A','C'],'I':['E','F','H','B','D']}
  dic={'A':{'C':'B','G':'D','I':'E'},'B':{'H':'E'},'C':{'A':'B','G':'E','I':'F'},'D':{'F':'E'},'E':{},'F':{'D':'E'},'G':{'A':'D','C':'E','I':'H'},'H':{'B':'E'},'I':{'A':'E','C':'F','G':'H'}}
  combination=[]
  new=''
  return(new_func(dic,firstPoint,length,new,graph,combination))
def new_func(dic,firstPoint,length,new,graph,combination):
        if length==1:return(1)
        elif firstPoint not in new:
            new+=firstPoint
            if len(new)==length:
                new = new[:-1]
                for val in graph[firstPoint]:
                    combination.append(new + val)
            elif len(new)==length-1:
                for element in graph[firstPoint]:
                    if element not in new:
                        combination.append(new+element)
                    elif element in new:
                        find=new[-1]
                        for key,value in dic[find].items():
                          if element==value:
                             if key not in new:
                                combination.append(new + key)
                new=new[:-1]
            else:
              for neighbour in graph[firstPoint]:
                new_func(dic,neighbour,length,new,graph,combination)
        else:
            find = new[-1]
            for key, value in dic[find].items():
                if firstPoint == value:
                    new_func(dic, key, length, new, graph, combination)
        return(len(combination))
print(count_patterns_from('E',8))