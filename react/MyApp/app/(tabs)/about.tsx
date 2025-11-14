
/* Name:Sarah Lam
File name:about.tsx
Description: This is the about page for the app. I talked about my hobbies in here

*/

import { StyleSheet } from 'react-native';
import {styles} from '../../assets/my_styles';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { Image } from 'react-native';
export default function About() {
  return (

    //gets the styling of the container, the title, and the body 
        <View style={styles.container}>
{/*the styling for the title  */}
      <Text style={styles.title}>About</Text>
      {/*the styling for the body from the styling sheet  */}
      <Text style={styles.body}>This app is about the type of noodles around the world. Many places around the world consume noodle dishes that are known to their location.Through this app, you will learn more about various dishes. </Text>
     
      <Image
      
                       source={require('@/assets/images/s.jpg')}
      
                      style={styles.image}
                  />
                   {/*the other body for below the image */}
                  <Text style={styles.body}>Many people enjoy eating noodles because of the enjoyable texture. </Text>
  
    </View>
  );
}

