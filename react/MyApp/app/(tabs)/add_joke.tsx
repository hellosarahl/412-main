

import React, {useState,useEffect} from 'react';
import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View} from '@/components/Themed';
import { ScrollView,StyleSheet,Image } from 'react-native';
import {styles} from '../../assets/my_styles';
import {TextInput,Button} from 'react-native';

/*Name:Sarah Lam
File:add_joke.tsx
Description:Collects a new joke and name of contributor
*/
export default function AddJokeScreen(){
      const[joke,setJoke]=useState('');
      const[con,setc]=useState('');
//submits the joke
      function submit(){
        fetch('http://10.239.55.12:8000/dadjokes/api/jokes',
            {method:"POST",
                body:JSON.stringify({
                    text:joke,
                    contributor:con
                })
                })
                .then(st=>console.log("st",st.status))
                .catch(e=>console.log('err',e));
      
    }

return (
    //the styles from the style sheet for cntainer 
    <View style={styles.container}>
      {/*the styling for the title from the style sheet */}
      <Text style={styles.title}>What is your joke?</Text>
         {/*text input of the joke */}
      <TextInput 
        placeholder="Type your joke here"
        value={joke}
        onChangeText={setJoke}
        style={styles.input}
        />
    <Text style={styles.title}>What is the contributor?</Text>
    {/*text input of the contirbutor */}
        <TextInput 
        placeholder="Name of Contributer"
        value={con}
        onChangeText={setc}
        style={styles.input}
        />
        <Button title="Submit" onPress={submit}/>
    



    </View>
  );
}

    


