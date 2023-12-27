/* https://leego.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%98%B8%ED%85%94-%EB%B0%A9-%EB%B0%B0%EC%A0%95-2019-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B2%A8%EC%9A%B8-%EC%9D%B8%ED%84%B4%EC%8B%AD-JavaScript
*/

function solution(k, room_number) {
  const rooms = new Map();

  const assignRooms = (num) => {
    if (!rooms.has(num)) {
      // 아직 배정받지 않은 방이라면, 다음 번호의 방을 담아준다.
      rooms.set(num, num + 1);
      return num;
    }
    // 이미 배정 받은 방이라면, 가리키고 있는 방이 배정 받았는지 확인한다.
    const nearestRoom = assignRooms(rooms.get(num));
    rooms.set(num, nearestRoom + 1);
    return nearestRoom;
  };

  return room_number.map(assignRooms);
}