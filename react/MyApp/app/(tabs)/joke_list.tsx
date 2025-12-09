
/* Name:Sarah Lam
File name:jokes_list.tsx
Description: This page shows a listing of all the jokes

*/

import React, {useState,useEffect} from 'react';
import { StyleSheet } from 'react-native';
import {styles} from '../../assets/my_styles';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { Image } from 'react-native';


export default function JokeListScreen() {
//stores the array of the jokes
  const[jokes,setJoke]=useState<any[]>([]);
  //const[pic,setPic]=useState<any>(null);
//fetch api for jokes
  useEffect(()=>{fetch('http://10.239.55.12:8000/dadjokes/api/jokes')
    .then(r=>r.json())
    .then (d=> setJoke(d))
    .catch(e=>console.log('Error',e));
  },[])



  return (
    //the styles from the style sheet for cntainer 
    <View style={styles.container}>
      {/*the styling for the title from the style sheet */}
      <Text style={styles.title}>LIST OF JOKES</Text>
         {/*the styling for the body from the style sheet */}
      <Text style={styles.body}></Text>
        {/*shows the jokes*/}
        {jokes.map(j=>(<Text key={j.id}>
          {j.text}
        </Text>
        ))}

          
    </View>
  );
}

