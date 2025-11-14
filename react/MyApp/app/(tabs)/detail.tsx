


import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View} from '@/components/Themed';
import { ScrollView,StyleSheet,Image } from 'react-native';
import {styles} from '../../assets/my_styles';

/*Name:Sarah Lam
File:detail.tsx
Description:An app for noodles. It shows example of types of noodles and the image'''
*/
export default function DetailScreen(){

    return(
    //from the style sheet for styling of the container 
    <ScrollView>
        <View style={styles.container}>
            {/*the styling for the title from the styling sheet */}
             <Text style={styles.title}>Detail</Text>
                <Text style={styles.body}> There are different type of noodles around the world.</Text>
            <Text>Below are examples around the world! </Text>



            {/*The styling from the body*/ }
            <Text style={styles.body}> Noodles in Italy such as Spaghetti.</Text>
{/*The styling from the image along with the image from external */ }
           <Image
                 source={{uri:'https://cs-people.bu.edu/sarahl/images/s.jpg'}}

                style={styles.image}
            />
                <Text style={styles.body}>

                Noodles in China such as Dan Dan noodles.</Text>
             <Image
                source={{uri:'https://cs-people.bu.edu/sarahl/images/d.jpg'}}

                style={styles.image}
            />
             <Text style={styles.body}>

                Noodles in Korea such as Cold Noodles.</Text>
             <Image
                source={{uri:'https://cs-people.bu.edu/sarahl/images/c.jpg'}}

                style={styles.image}
                />

        </View>
        </ScrollView>

    );

}

