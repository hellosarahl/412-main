

/*Name:Sarah Lam 
File:index.tsx
Description: This is the index of my project.This is where I talk about myself */


import { StyleSheet,Image } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import {styles} from '../../assets/my_styles';


export default function IndexScreen() {
  return (
    //the styles from the style sheet for cntainer 
    <View style={styles.container}>
      {/*the styling for the title from the style sheet */}
      <Text style={styles.title}>Index</Text>
         {/*the styling for the body from the style sheet */}
      <Text style={styles.body}>Hi, I am Sarah! I enjoy exploring new places and trying new cusines. My favorite animal are bunnies!</Text>
           {/*the styling for the image from the style sheet and the image from the directory */}
      
      <Image
                      source={require('@/assets/images/bunnies.jpg')}
      
                      style={styles.image}
                  />
    </View>
  );
}


