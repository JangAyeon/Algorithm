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