'''File:voter_analytics views.py
Author:Sarah Lam
Description:views.py for the voter_analytics to display info'''

from django.shortcuts import render



# Create your views here.
from django.db.models.query import QuerySet
from django.views.generic import ListView,DetailView
from .models import Voter
import plotly
import plotly.graph_objs as go

'''provides list of voter records'''
class VoterListView(ListView):
    #show results with list views
    model=Voter
    template_name='voter_analytics/voter_list.html'
    context_object_name='voters'
    # the amount of records per page 
    paginate_by=100




    '''query set'''
    def get_queryset(self):
        #limit the result query set
       queryset=super().get_queryset()
        #slice returns first 100
        #return results[:100]
        # look for the url paramters to filter by

       city=self.request.GET.get('city')

       if city:
             queryset=queryset.filter(v21town__icontains=city)

       party=self.request.GET.get('party_aff')
       if party:
           queryset=queryset.filter(party_aff=party)

        #the birth years
       min_birth=self.request.GET.get('min_birth')
       max_birth=self.request.GET.get('max_birth')
       if min_birth:
           try:
               year=int(min_birth)
               queryset=queryset.filter(birth__year=year)
           except ValueError:
               pass
   
        
       if max_birth:
           try:
               year=int(max_birth)
               queryset=queryset.filter(birth__year=year)
           except ValueError:
               pass

        #votes
       voter_score=self.request.GET.get('voter_score')
       if voter_score:
           try:
               score=int(voter_score)
               queryset=queryset.filter(voter_score=score)
           except ValueError:
               pass
        

    
    #election
       e=self.request.GET.get('election2020')
       if e in ['True']:
           queryset=queryset.filter(v20state=True)

       election=self.request.GET.get('election2022')
       if election in ['True']:
            queryset=queryset.filter(v22general=True)

       return queryset
           
   

       
        
      
    


'''class to show the result of a single voter'''
class VoterDetailView(DetailView):
       '''displays the result for a single voter'''
       model=Voter
       #this is for results
       context_object_name='voter'
       template_name='voter_analytics/voter_detail.html'


       def get_context_data(self, **kwargs):
           '''provide context var for use in template'''
           context=super().get_context_data(**kwargs)
           # result for one voter
           r=context['voter']

           # create grpah of first hald/second half of pie chart
           labels=['first half', 'second half']
           first_half_seconds=(r.time_half1.hour* 3600)+(r.time_half1.minute* 60)+r.time_half1.second 
           second_half_seconds=(r.time_half2.hour * 3600)+(r.time_half2.minute *60)+r.time_half2.second
           values=[first_half_seconds, second_half_seconds]

           #the pie chart 
           fig=go.Figure(go.Pie(labels=labels,values=values))
           fig.update_layout(title_text="Half Voter Splits")
           #get the graph at the html div 
           graph_div_splits=plotly.offline.plot(fig,
                                                 auto_open=False,
                                                 output_type="div")
                                                 
            # div is template context var
           context['graph_div_splits']=graph_div_splits
           #create a bar chart with count of runners passed/passed by 
           x=[f'Runners Passed By {r.first_name}',
              f' Runners who Passed {r.first_name}']
           
           y=[r.get_runners_passed(),
              r.get_runners_passed_by()]
           
           fig=go.Figure(go.Bar(x=x,y=y))
           fig.update_layout(title_text="Runners passed/passed by")
    
           graph_div_passed=plotly.offline.plot(fig,
                                                 auto_open=False,output_type="div"
                                                 )
           
           context["graph_div_passed"]=graph_div_passed
                                                
           
           return context 
       
'''Displays the graph view of the outcomes '''
class GraphsView(ListView):
    model=Voter
    template_name='voter_analytics/graphs.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)



        #bar chart 
        # bar chart of the distribution
        birth=list(Voter.objects.values_list('birth__year',flat=True))
        u=list(set(birth))

        #the voters for every city 
        counts=[]
        for year in u:
            count=0
            for c in birth:
                if c==year:
                    count+=1
            counts.append(count)


        fig=go.Figure(go.Bar(x=u,y=counts))
        fig.update_layout(title_text="Voters by birth")


        graphs=plotly.offline.plot(fig,auto_open=False,output_type="div"
                        )
           
        context["graphs"]= graphs


        #pie chart
        party=list(Voter.objects.values_list('party_aff',flat=True))
        u=list(set(party))

        #the voters for every city 
        counts=[]
        for p in u:
            count=0
            for c in party:
                if c==p:
                    count+=1
            counts.append(count)


        fig=go.Figure(go.Pie(labels=u,values=counts))
        fig.update_layout(title_text="Voters by affiliations")


        graph_party=plotly.offline.plot(fig,auto_open=False,output_type="div"
                        )
           
        context["graph_party"]= graph_party


        # bar chart of the distribution

        cities=list(Voter.objects.values_list('v21town',flat=True))
        u=list(set(cities))

        #the voters for every city 
        counts=[]
        for city in u:
            count=0
            for c in cities:
                if c==city:
                    count+=1
            counts.append(count)


        fig=go.Figure(go.Bar(x=u,y=counts))
        fig.update_layout(title_text="Voters for city")


        graph_distribution=plotly.offline.plot(fig,auto_open=False,output_type="div"
                        )
           
        context["graph_distribution"]= graph_distribution






                                                
           
        return context 
       




              

  
       

          
    



