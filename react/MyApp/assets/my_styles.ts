/*
Name:Sarah Lam 
File: my_styles.ts
Decription: Style sheet for my entire project such as the other components like the title, bodyt, and the images
*/
import {StyleSheet} from 'react-native';

export const styles = StyleSheet.create({
    /* allows styling to the contained info */
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
   /* allows styling to the title of each tsx of index,about, detail */
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color:'blue',
  },
  /* allows styling to the body paragraoh */

  body: {
    fontSize: 17,
    textAlign: 'center',

  },
  
/*allows styling to the images */
  image: {
   width:100,height:100, marginTop:10
  },

  //for the styles of the text
  input:{
    height:40,
    color:'black',
    backgroundColor:'white'
  }
});