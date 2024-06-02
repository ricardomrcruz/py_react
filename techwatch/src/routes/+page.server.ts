import { posts1 } from './data1';
import { posts2 } from './data2';

interface Post {
  title: string;
  price: string;
  description: string;
  link: string;
  img: string;
}

export function load(): { posts1: Post[], posts2: Post[] } {
  console.log('posts1 from data1:', posts1); // Debug log
  console.log('posts2 from data2:', posts2); // Debug log

  const mappedPosts1 = posts1.map((post) => ({
    title: post.title,
    price: post.price,
    description: post.description,
    link: post.link,
    img: post.img,
  }));

  const mappedPosts2 = posts2.map((post) => ({
    title: post.title,
    price: post.price,
    description: post.description,
    link: post.link,
    img: post.img,
  }));

  console.log('mappedPosts1:', mappedPosts1); // Debug log
  console.log('mappedPosts2:', mappedPosts2); // Debug log

  return {
    posts1: mappedPosts1,
    posts2: mappedPosts2,
  };
}
