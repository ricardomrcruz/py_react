import { posts1} from './data1'
import { posts2} from './data2'

export function load(){
    return {
         posts1: posts1.map((post) => ({
            title: post.title,
            price: post.price,
            description: post.description,
            link: post.link,
            img: post.img,

         })),

         posts2: posts2.map((post) => ({
            title: post.title,
            price: post.price,
            description: post.description,
            link: post.link,
            img: post.img,

         }))

    }
}
