

/*Name:Sarah Lam 
File:index.tsx
Description: Shows single joke and a picture */

import React, {useState,useEffect} from 'react';
import { StyleSheet,Image } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import {styles} from '../../assets/my_styles';


export default function IndexScreen() {
//store the  joke and pics from api
  const[joke,setJoke]=useState<any>(null);
  const[pic,setPic]=useState<any>(null);

//fetch joke from the api
  useEffect(()=>{fetch('http://10.239.55.12:8000/dadjokes/api/random')
    .then(r=>{
      //debug
      console.log('joke status',r.status);
      return r.json();
    })
   
    .then (d=>setJoke(d))
    .catch(e=>console.log('Error',e))

//fetching of random pic fromapi
    fetch('http://10.239.55.12:8000/dadjokes/api/random_picture')
    .then(r=>r.json())
    .then (d=>{
      console.log('pic',d);
      setPic(d);
    })
     .catch(e=>console.log('Error',e));
    },[]);



  return (
    //the styles from the style sheet for cntainer 
    <View style={styles.container}>
      {/*the styling for the title from the style sheet */}
      <Text style={styles.title}>Index</Text>
         {/*the styling for the body from the style sheet */}
      <Text style={styles.body}>
        {joke? joke.text:'This is loading'}
        </Text>

           {/*the styling for the image from the style sheet and the image from the directory */}
           
      {pic?.image &&(
      <Image
                      source={{uri:pic.image}}
                      
                      style={styles.image}
                  />
      )}
    </View>
  );
}


