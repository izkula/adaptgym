mazes = {}
vars = {}
height = {}
walls = {}
# x is left/right

mazes[0] = "**********************\n" \
           "****               ***\n" \
           "*                   **\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     *    0       G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*  *                **\n" \
           "**********************\n"
vars[0] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

mazes[1] = "**********************\n" \
           "****               ***\n" \
           "*                   **\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2   ***  4     *\n" \
           "*                    *\n" \
           "*              *     *\n" \
           "*     *    0   *   G *\n" \
           "*              *     *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*  *                **\n" \
           "**********************\n"
vars[1] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


mazes[2] = "**********************\n" \
           "****               ***\n" \
           "*                   **\n" \
           "*                    *\n" \
           "*         ******     *\n" \
           "*     ****     *     *\n" \
           "*     *        *     *\n" \
           "*     *        *     *\n" \
           "*     *   ***  *     *\n" \
           "*         *    *     *\n" \
           "*        **    *     *\n" \
           "*     *  * 0   *   G *\n" \
           "*     *  *     *     *\n" \
           "*     *  *     *     *\n" \
           "*     *  *     *     *\n" \
           "*     *        *     *\n" \
           "*     *        *     *\n" \
           "*     *        *     *\n" \
           "*              *     *\n" \
           "****************     *\n" \
           "*  *                **\n" \
           "**********************\n"
vars[2] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

mazes[3] = "**********************\n" \
           "****           2   ***\n" \
           "*                   **\n" \
           "*  3                 *\n" \
           "*         ******     *\n" \
           "*     ****     *     *\n" \
           "*     *        *     *\n" \
           "*     *        *     *\n" \
           "*     *   ***  *     *\n" \
           "*         *    *     *\n" \
           "*        **    *     *\n" \
           "*     *  * 0   *   G *\n" \
           "*     *  *     *     *\n" \
           "*     *  *     *     *\n" \
           "*     *  *     *     *\n" \
           "*     *        *     *\n" \
           "*     *     5  *  4  *\n" \
           "*     *        *     *\n" \
           "*              *     *\n" \
           "****************     *\n" \
           "*  *                **\n" \
           "**********************\n"
vars[3] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

mazes[4] = "********************\n" \
           "**               ***\n" \
           "*                 **\n" \
           "*         50       *\n" \
           "*     2            *\n" \
           "*     6    4       *\n" \
           "*     3            *\n" \
           "*   *            G *\n" \
           "*           d      *\n" \
           "*   7              *\n" \
           "*    8    b        *\n" \
           "*     9      $     *\n" \
           "*c********A  a    **\n" \
           "********************\n"
height[4]= "55555555555555555555\n" \
           "51               295\n" \
           "5                 35\n" \
           "5          3       5\n" \
           "5                  5\n" \
           "5                  5\n" \
           "5                  5\n" \
           "5   9              5\n" \
           "5                  5\n" \
           "5                  5\n" \
           "5                  5\n" \
           "5                  5\n" \
           "5123456789        35\n" \
           "55555555555555555555\n"
walls[4] = "********************\n" \
           "**               ***\n" \
           "*                 **\n" \
           "*          &       *\n" \
           "*                  *\n" \
           "*                  *\n" \
           "*                  *\n" \
           "*   *              *\n" \
           "*                  *\n" \
           "*                  *\n" \
           "*                  *\n" \
           "*                  *\n" \
           "*&^%*&^%*&        **\n" \
           "********************\n"
vars[4] =  "....................\n" \
           ".BAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAA.\n" \
           "....................\n"

height[5]= "5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5         333        5\n" \
           "5                    5\n" \
           "5              4     5\n" \
           "5  4321        2     5\n" \
           "5              3     5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[5] = "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*         ***        *\n" \
           "*                    *\n" \
           "*              *     *\n" \
           "*  ****    0   *   G *\n" \
           "*              *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[5] = "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^         ^^^        &\n" \
           "^                    &\n" \
           "^              ^     &\n" \
           "^  &*%^        *     &\n" \
           "^              %     &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "**********************\n"
vars[5] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


height[6]="5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555888555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555559555555\n" \
           "5559876555555557555555\n" \
           "5555555555555558555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n" \
           "5555555555555555555555\n"
mazes[6] = "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*         ***        *\n" \
           "*                    *\n" \
           "*              *     *\n" \
           "*  ****    0   *   G *\n" \
           "*              *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[6] = "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^*********^^^********&\n" \
           "^********************&\n" \
           "^**************^*****&\n" \
           "^**&*%^********^*****&\n" \
           "^**************%*****&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "^********************&\n" \
           "**********************\n"
vars[6] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


height[7]= "5555555555555555555555\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5              4     5\n" \
           "5  4321        2     5\n" \
           "5              3     5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[7] = "**********************\n" \
           "*          G         *\n" \
           "*********** **********\n" \
           "*           5        *\n" \
           "*                    *\n" \
           "*********** **********\n" \
           "*          4         *\n" \
           "*                    *\n" \
           "*********** **********\n" \
           "*          2         *\n" \
           "*              *     *\n" \
           "*  ****    0   *     *\n" \
           "*              *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[7] = "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "^                    &\n" \
           "^^^%%^^%^^^ &%*&*%%*%&\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^^^^^^^^^^^ &&*&*&&*&&\n" \
           "^                    &\n" \
           "^                    &\n" \
           "&&&&&&&&&&& %%%%%%%%%&\n" \
           "^                    &\n" \
           "^              ^     &\n" \
           "^  &*%^        *     &\n" \
           "^              %     &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "**********************\n"
vars[7] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[8]= "5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[8] = "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*          0       G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[8] = "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "**********************\n"
vars[8] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"



height[9]= "5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[9] = "**********************\n" \
           "*                    *\n" \
           "*   G                *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*          0         *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[9] = "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "^                    &\n" \
           "**********************\n"
vars[9] =  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


height[10]="5555555555555555555555\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5              4     5\n" \
           "5  4321        2     5\n" \
           "5              3     5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[10] = "**********************\n" \
           "*   G                *\n" \
           "*********** **********\n" \
           "*          5         *\n" \
           "*                    *\n" \
           "*********** **********\n" \
           "*          4         *\n" \
           "*                    *\n" \
           "*********** **********\n" \
           "*          3         *\n" \
           "*              *     *\n" \
           "*  ****    0   *     *\n" \
           "*              *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              2     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[10] ="&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&^^%%^^%^^^ &%*&*%%*%&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&^^^^^^^^^^ &&*&*&&*&&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&& %%%%%%%%%&\n" \
           "&                    &\n" \
           "&              ^     &\n" \
           "&  &*%^        *     &\n" \
           "&              %     &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[10] = "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[11]="5555555555555555555555\n" \
           "5                    5\n" \
           "5555555555555555555555\n" \
           "5             4      5\n" \
           "5             3      5\n" \
           "5             2      5\n" \
           "5             1      5\n" \
           "5                    5\n" \
           "5555555555555555555555\n" \
           "5     4              5\n" \
           "5     3        4     5\n" \
           "5     2        2     5\n" \
           "5     1        3     5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[11] ="**********************\n" \
           "*   G                *\n" \
           "**********************\n" \
           "*             *      *\n" \
           "*             *      *\n" \
           "*             *      *\n" \
           "*             *      *\n" \
           "*                    *\n" \
           "**********************\n" \
           "*     *              *\n" \
           "*     *    3   *     *\n" \
           "*     *    0   *     *\n" \
           "*     *        *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              2     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[11] ="&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&^^^^^^^^^^^^^^^^^^^^&\n" \
           "&             &      &\n" \
           "&             *      &\n" \
           "&             %      &\n" \
           "&             ^      &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&     &              &\n" \
           "&     *        ^     &\n" \
           "&     %        *     &\n" \
           "&     ^        %     &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[11] = "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[12]="5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n" \
           "566666 1             5\n" \
           "566666555555 555555555\n" \
           "5     4           4  5\n" \
           "5     3           3  5\n" \
           "5     2           2  5\n" \
           "5     1           1  5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[12] ="**********************\n" \
           "*   G                *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n" \
           "****** *             *\n" \
           "******3***** *********\n" \
           "*     *           *  *\n" \
           "*     *           *  *\n" \
           "*     *    0      *  *\n" \
           "*     *           *  *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              2     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[12] ="&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&&&&&& &             &\n" \
           "&&&&&&&&&&&& &&&&&&&&&\n" \
           "&     &           &  &\n" \
           "&     *           *  &\n" \
           "&     %           %  &\n" \
           "&     ^           ^  &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[12] = "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[13]="5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n" \
           "511111 1             5\n" \
           "566666555555 555555555\n" \
           "5     4           4  5\n" \
           "5     3           3  5\n" \
           "5     2           2  5\n" \
           "5     1           1  5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[13] ="**********************\n" \
           "*   G                *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n" \
           "****** *             *\n" \
           "******3***** *********\n" \
           "*     *           *  *\n" \
           "*     *           *  *\n" \
           "*     *    0      *  *\n" \
           "*     *           *  *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              2     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[13] ="&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&&&&&& &             &\n" \
           "&&&&&&&&&&&& &&&&&&&&&\n" \
           "&     &           &  &\n" \
           "&     *           *  &\n" \
           "&     %           %  &\n" \
           "&     ^           ^  &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[13] = "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"



height[14]="5555555555555555555555\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "55555555555 5555555555\n" \
           "5                    5\n" \
           "5              4     5\n" \
           "5  4321        2     5\n" \
           "5              3     5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[14] = "**********************\n" \
           "*          G         *\n" \
           "*********** **********\n" \
           "*          5         *\n" \
           "*                    *\n" \
           "*********** **********\n" \
           "*          4         *\n" \
           "*                    *\n" \
           "*********** **********\n" \
           "*          3         *\n" \
           "*              *     *\n" \
           "*  ****        *   0 *\n" \
           "*              *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              2     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[14] ="&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&^^%%^^%^^^ &%*&*%%*%&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&^^^^^^^^^^ &&*&*&&*&&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&& %%%%%%%%%&\n" \
           "&                    &\n" \
           "&              ^     &\n" \
           "&  &*%^        *     &\n" \
           "&              %     &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[14] = "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


height[15]="5555555555555555555555\n" \
           "5                    5\n" \
           "5555555555555555555555\n" \
           "5     4              5\n" \
           "5     3              5\n" \
           "5     2              5\n" \
           "5     1              5\n" \
           "5                    5\n" \
           "5555555555555555555555\n" \
           "5     4              5\n" \
           "5     3        4     5\n" \
           "5     2        2     5\n" \
           "5     1        3     5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[15] ="**********************\n" \
           "*   G                *\n" \
           "**********************\n" \
           "*     *              *\n" \
           "*     *              *\n" \
           "*     *              *\n" \
           "*     *              *\n" \
           "*                    *\n" \
           "**********************\n" \
           "*     *              *\n" \
           "*     *    3   *     *\n" \
           "*     *    0   *     *\n" \
           "*     *        *     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              2     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[15] ="&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&^^^^^^^^^^^^^^^^^^^^&\n" \
           "&     &              &\n" \
           "&     *              &\n" \
           "&     %              &\n" \
           "&     ^              &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&     &              &\n" \
           "&     *        ^     &\n" \
           "&     %        *     &\n" \
           "&     ^        %     &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[15] = "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[16]= "5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[16]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*          0       G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[16]= "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[16]=  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[16_2] = height[16]
mazes[16_2] = mazes[16]
vars[16_2] = vars[16]
walls[16_2]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"

height[17]= "5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[17]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*      4             *\n" \
           "*        2           *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*          0       G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*        5           *\n" \
           "*      3             *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[17]= "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[17]=  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[18]=  "999999999999999999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9999 99999999999 9999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9999 99999999999 9999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999999999999999\n"
mazes[18] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "**** *********** ****\n" \
             "*   4           5   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "**** *********** ****\n" \
             "*   2           3   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

walls[18] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "**** *********** ****\n" \
             "*   4           5   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "**** *********** ****\n" \
             "*   2           3   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

vars[18] =   ".....................\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".....................\n"


height[19]=  "999999999999999999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9999999 99999 9999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9999999 99999 9999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999999999999999\n"
mazes[19] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*      4     5      *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*      2     3      *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

walls[19] =  "*********************\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

vars[19] =   ".....................\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".....................\n"

height[20]=  "999999999999999999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9999999 99999 9999999\n" \
             "9    9   9 9   9    9\n" \
             "9     9 9   9 9     9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9999999 99999 9999999\n" \
             "9    9   9 9   9    9\n" \
             "9     9 9   9 9     9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999999999999999\n"
mazes[20] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*    * 4 * * 5 *    *\n" \
             "*     * *   * *     *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*    * 2 * * 3 *    *\n" \
             "*     * *   * *     *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

walls[20] =  "*********************\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*    *   * *   *    *\n" \
             "*     * *   * *     *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "******* ***** *******\n" \
             "*    *   * *   *    *\n" \
             "*     * *   * *     *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*********************\n"

vars[20] =   ".....................\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".....................\n"


height[21]=  "999999999999999999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999 9 999999999\n" \
             "9         9         9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999 9 999999999\n" \
             "9         9         9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999999999999999\n"
mazes[21] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*        4*5        *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*        2*3        *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

walls[21] =  "*********************\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*         *         *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*         *         *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

vars[21] =   ".....................\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".....................\n"


height[22]=  "999999999999999999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999999999999999\n"
mazes[22] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

walls[22] =  "*********************\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*********************\n"

vars[22] =   ".....................\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAA.\n" \
             ".....................\n"

height[23]=  "999999999999999999999\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999 9 999999999\n" \
             "9         9         9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "9                   9\n" \
             "999999999999999999999\n"
mazes[23] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*        2*3        *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*         0         *\n" \
             "*                   *\n" \
             "*********************\n"

walls[23] =  "*********************\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*         *         *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*********************\n"
vars[23] =  vars[21]

height[24] = height[23]
walls[24] = walls[23]
vars[24] = vars[23]
mazes[24] =  "*********************\n" \
             "*                   *\n" \
             "*         G         *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "********* * *********\n" \
             "*        2*3        *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*                   *\n" \
             "*        0          *\n" \
             "*                   *\n" \
             "*********************\n"



height[25]="5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[25]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*         0        G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[25]= "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[25]=  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"

height[252]="55555555555555555555555\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "5                     5\n" \
           "55555555555555555555555\n"
mazes[252]= "***********************\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*     2         4     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*          0        G *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*     5         3     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "*                     *\n" \
           "***********************\n"
walls[252]= "&&&&&&&&&&&&&&&&&&&&&&&\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "*                     &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&&\n"
vars[252]=  ".......................\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAAA.\n" \
           ".......................\n"


height[251]="5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[251]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2      4       *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     0         5  G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*            3       *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[251]= "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&\n"
vars[251]=  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


height[26]="5555555555555555555555\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5999999999   999999995\n" \
           "5999999999   999999995\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5                    5\n" \
           "5555555555555555555555\n"
mazes[26]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     2        4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*         0        G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*     5        3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********   *********\n" \
           "**********   *********\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"
walls[26]= "&&&&&&&&&&&&&&&&&&&&&&\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*&&&&&&&&&   &&&&&&&&&\n" \
           "*&&&&&&&&&   &&&&&&&&&\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "*                    &\n" \
           "%%%%%%%%%%%%%%%%%%%%%%\n"
vars[26]=  "......................\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA.\n" \
           "......................\n"


height[27] = height[25]
walls[27] = walls[25]
vars[27] = vars[25]
mazes[27]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                  G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*   0          3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"

height[28] = height[25]
walls[28] = walls[25]
vars[28] = vars[25]
mazes[28]= "**********************\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*   0          4     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                  G *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*              3     *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "*                    *\n" \
           "**********************\n"



height[29]="55555555555555555555555555555555555555555555\n" \
           "5    555555555555    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5         55151  1   99                    5\n" \
           "5   1234  5      1   99                    5\n" \
           "5         5      1   99                    5\n" \
           "5         5          99                    5\n" \
           "5                    99                    5\n" \
           "5                                          5\n" \
           "5                                          5\n" \
           "5                                          5\n" \
           "5                    99                    5\n" \
           "5         5          99                    5\n" \
           "5         5      1   99                    5\n" \
           "5   1234  5      1   99                    5\n" \
           "5         55151  1   99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5    555555555555    99                    5\n" \
           "55555555555555555555555555555555555555555555\n"
mazes[29]= "********************************************\n" \
           "*    ************    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*         *****  *   **     2        4     *\n" \
           "*   ****  *      *   **                    *\n" \
           "*         *      *   **                    *\n" \
           "*         *          **                    *\n" \
           "*                    **                    *\n" \
           "*                                          *\n" \
           "*                               0        G *\n" \
           "*                                          *\n" \
           "*                    **                    *\n" \
           "*         *          **                    *\n" \
           "*         *      *   **                    *\n" \
           "*   ****  *      *   **                    *\n" \
           "*         *****  *   **     5        3     *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*    ************    **                    *\n" \
           "********************************************\n"
walls[29]= "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n" \
           "%    ^^^^^^^^^^^^    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%         @@@@@  %   **                    &\n" \
           "%   &^&^  @      %   **                    &\n" \
           "%         @      %   **                    &\n" \
           "%         @          **                    &\n" \
           "%                    **                    &\n" \
           "%                                          &\n" \
           "%                                          &\n" \
           "%                                          &\n" \
           "%                    **                    &\n" \
           "%         @          **                    &\n" \
           "%         @      %   **                    &\n" \
           "%   &^&^  @      %   **                    &\n" \
           "%         @@@@@  %   **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%    ^^^^^^^^^^^^    **                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n"
vars[29]=  "............................................\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           "............................................\n"

height[30]="55555555555555555555555555555555555555555555\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                                          5\n" \
           "5                                          5\n" \
           "5                                          5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "55555555555555555555555555555555555555555555\n"
mazes[30]= "********************************************\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **     2        4     *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                                          *\n" \
           "*                               0        G *\n" \
           "*                                          *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **     5        3     *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "********************************************\n"
walls[30]= "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                                          &\n" \
           "%                                          &\n" \
           "%                                          &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n"
vars[30]=  "............................................\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           "............................................\n"

height[31]="55555555555555555555555555555555555555555555\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "5     999999999999   99                    5\n" \
           "5     9          9   99                    5\n" \
           "5     9         39   99                    5\n" \
           "5     9   99999999   99                    5\n" \
           "5     9              99                    5\n" \
           "5     99999999999999999                    5\n" \
           "5                                          5\n" \
           "5                                          5\n" \
           "5                                          5\n" \
           "5     99999999999999999                    5\n" \
           "5     9              99                    5\n" \
           "5     9   99999999   99                    5\n" \
           "5     9         39   99                    5\n" \
           "5     9          9   99                    5\n" \
           "5     999999999999   99                    5\n" \
           "5                    99                    5\n" \
           "5                    99                    5\n" \
           "55555555555555555555555555555555555555555555\n"
mazes[31]= "********************************************\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "*     ************   **                    *\n" \
           "*     *          *   **     2        4     *\n" \
           "*     *         **   **                    *\n" \
           "*     *   ********   **                    *\n" \
           "*     *              **                    *\n" \
           "*     *****************                    *\n" \
           "*                                          *\n" \
           "*                               0        G *\n" \
           "*                                          *\n" \
           "*     *****************                    *\n" \
           "*     *              **                    *\n" \
           "*     *   ********   **                    *\n" \
           "*     *         **   **                    *\n" \
           "*     *          *   **     5        3     *\n" \
           "*     ************   **                    *\n" \
           "*                    **                    *\n" \
           "*                    **                    *\n" \
           "********************************************\n"
walls[31]= "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "%     ***%*%*%*%**   **                    &\n" \
           "%     @          *   **                    &\n" \
           "%     @         %*   **                    &\n" \
           "%     @   ^%*^%***   **                    &\n" \
           "%     @              **                    &\n" \
           "%     *****************                    &\n" \
           "%                                          &\n" \
           "%                                          &\n" \
           "%                                          &\n" \
           "%     *****************                    &\n" \
           "%     @              **                    &\n" \
           "%     @   %^*%^***   **                    &\n" \
           "%     @         ^*   **                    &\n" \
           "%     @          *   **                    &\n" \
           "%     ***^*^*^*^**   **                    &\n" \
           "%                    **                    &\n" \
           "%                    **                    &\n" \
           "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n"
vars[31]=  "............................................\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           ".AAAAAAAAAAAAAAAAAAAA..AAAAAAAAAAAAAAAAAAAA.\n" \
           "............................................\n"

height[100]= "999999999999999999999 \n" \
             "9                    9\n" \
             "9                    9\n" \
             "9   99999    99999   9\n" \
             "9      99    99      9\n" \
             "9      99    99      9\n" \
             "9      99    99      9\n" \
             "9      99    99      9\n" \
             "9      99    99      9\n" \
             "9      99    99      9\n" \
             "9      99    99      9\n" \
             "999999999    999999999\n" \
             "9                    9\n" \
             "9                    9\n" \
             "9                    9\n" \
             "9                    9\n" \
             "9                    9\n" \
             "9                    9\n" \
             "9                    9\n" \
             "9          0         9\n" \
             "9                    9\n" \
             "9999999999999999999999\n"
mazes[100] = "*********************G\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*   *****    *****   *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*   2  **    **  3   *\n" \
             "*      **    **      *\n" \
             "*********    *********\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*          0         *\n" \
             "*                    *\n" \
             "**********************\n"

walls[100] = "********************* \n" \
             "*                    *\n" \
             "*                    *\n" \
             "*   *****    *****   *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*      **    **      *\n" \
             "*********    *********\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "*                    *\n" \
             "**********************\n"

vars[100] =  "......................\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             "......................\n"

height[101] = "9999999999999999999999\n" \
              "9        9999        9\n" \
              "9  9  9  9999  9  9  9\n" \
              "9  9  9999999999  9  9\n" \
              "9999              9999\n" \
              "9999  9999  9999  9999\n" \
              "9  9  9  9  9  9  9  9\n" \
              "9  9  9  9  9  9  9  9\n" \
              "9        9  9        9\n" \
              "9999999999  9999999999\n" \
              "90          999999999 \n" \
              "9999999999  9999999999\n" \
              "9        9  9        9\n" \
              "9  9  9  9  9  9  9  9\n" \
              "9  9  9  9  9  9  9  9\n" \
              "9999  9999  9999  9999\n" \
              "9999              9999\n" \
              "9999  9999999999  9999\n" \
              "9  9  9  9999  9  9  9\n" \
              "9  9  9  9999  9  9  9\n" \
              "9        9999        9\n" \
              "9999999999999999999999\n"

mazes[101] = "**********************\n" \
             "*        ****        *\n" \
             "*  *  *  ****  *  *  *\n" \
             "*  *  **********  *  *\n" \
             "****              ****\n" \
             "****  ****  ****  ****\n" \
             "*  *  *  *  *  *  *  *\n" \
             "*  *  *  *  *  *  *  *\n" \
             "*        *  *        *\n" \
             "**********  **********\n" \
             "*0          *********G\n" \
             "**********  **********\n" \
             "*        *  *        *\n" \
             "*  *  *  *  *  *  *  *\n" \
             "*  *  *  *  *  *  *  *\n" \
             "****  ****  ****  ****\n" \
             "****              ****\n" \
             "****  **********  ****\n" \
             "*  *  *  ****  *  *  *\n" \
             "*  *  *  ****  *  *  *\n" \
             "*        ****        *\n" \
             "**********************\n"

walls[101] = "**********************\n" \
             "*        ****        *\n" \
             "*  *  *  ****  *  *  *\n" \
             "*  *  **********  *  *\n" \
             "****              ****\n" \
             "****  ****  ****  ****\n" \
             "*  *  *  *  *  *  *  *\n" \
             "*  *  *  *  *  *  *  *\n" \
             "*        *  *        *\n" \
             "**********  **********\n" \
             "*0          ********* \n" \
             "**********  **********\n" \
             "*        *  *        *\n" \
             "*  *  *  *  *  *  *  *\n" \
             "*  *  *  *  *  *  *  *\n" \
             "****  ****  ****  ****\n" \
             "****              ****\n" \
             "****  **********  ****\n" \
             "*  *  *  ****  *  *  *\n" \
             "*  *  *  ****  *  *  *\n" \
             "*        ****        *\n" \
             "**********************\n"

vars[101] =  "......................\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             ".AAAAAAAAAAAAAAAAAAAA.\n" \
             "......................\n"

###################################################################################################
###################################################################################################

height['object_appear'] =   "9999999999999999999999\n" \
                            "9                    9\n" \
                            "9999999999999999999999\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9                    9\n" \
                            "9999999999999999999999\n"

mazes['object_appear'] =    "**********************\n" \
                             "*   2                *\n" \
                             "**********************\n" \
                             "*  1                 *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*         0        G *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "**********************\n"

walls['object_appear'] =     "**********************\n" \
                             "*                    *\n" \
                             "**********************\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "*                    *\n" \
                             "**********************\n"

vars['object_appear'] =      "......................\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             "......................\n"

###################################################################################################

height['dynamics'] =  "9999999999999999999999\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9999999999999999999999\n"

mazes['dynamics'] =  "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*     1        2     *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*         0          *\n" \
                     "*                    G\n" \
                     "*    1               *\n" \
                     "*                    *\n" \
                     "*              2     *\n" \
                     "*                    *\n" \
                     "*     2              *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*          1         *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "**********************\n"

# mazes['dynamics'] =  "**********************\n" \
#                      "*                    *\n" \
#                      "*                    *\n" \
#                      "*     1              *\n" \
#                      "*                    *\n" \
#                      "*                    *\n" \
#                      "*      0  0000000    *\n" \
#                      "*         00000000   *\n" \
#                      "*    0    000 2 000  *\n" \
#                      "*         000000 0   *\n" \
#                      "*                    G\n" \
#                      "*    1    0          *\n" \
#                      "*                    *\n" \
#                      "*              2     *\n" \
#                      "*                    *\n" \
#                      "*     2              *\n" \
#                      "*                    *\n" \
#                      "*                    *\n" \
#                      "*          1         *\n" \
#                      "*                    *\n" \
#                      "*                    *\n" \
#                      "**********************\n"

walls['dynamics'] =  "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                     \n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "**********************\n"

vars['dynamics'] =   "......................\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     "......................\n"

##################################################################################

height['corridor'] =  "9999999999999999999999\n" \
                          "9    5               9\n" \
                          "9    5               9\n" \
                          "9    55555555555     9\n" \
                          "9              5     9\n" \
                          "9              5     9\n" \
                          "9              5     9\n" \
                          "95555555555    5     9\n" \
                          "9         5    5     9\n" \
                          "9555555   5    5     9\n" \
                          "9     5   5          9\n" \
                          "9     5   5          9\n" \
                          "9     5   5          9\n" \
                          "9     5   5          9\n" \
                          "9                    9\n" \
                          "9                    9\n" \
                          "95555         55     9\n" \
                          "9   5         55     9\n" \
                          "9   555555555555     9\n" \
                          "9                    9\n" \
                          "9                    9\n" \
                          "9999999999999999999999\n"

mazes['corridor'] =  "**********************\n" \
                         "*    *               *\n" \
                         "*    *               *\n" \
                         "*    ***********     *\n" \
                         "*              *     *\n" \
                         "*              *     *\n" \
                         "*              *     *\n" \
                         "***********    *     *\n" \
                         "*         *    *     *\n" \
                         "*******   *    *     *\n" \
                         "*     *   *          G\n" \
                         "*     *   *          *\n" \
                         "*     *   *          *\n" \
                         "*     *   *          *\n" \
                         "*            0       *\n" \
                         "*                    *\n" \
                         "*****         **     *\n" \
                         "*   *         **     *\n" \
                         "*   ************     *\n" \
                         "*                    *\n" \
                         "*                    *\n" \
                         "**********************\n"

walls['corridor'] =  "**********************\n" \
                         "*    *               *\n" \
                         "*    *               *\n" \
                         "*    ***********     *\n" \
                         "*              *     *\n" \
                         "*              *     *\n" \
                         "*              *     *\n" \
                         "***********    *     *\n" \
                         "*         *    *     *\n" \
                         "*******   *    *     *\n" \
                         "*     *   *           \n" \
                         "*     *   *          *\n" \
                         "*     *   *          *\n" \
                         "*     *   *          *\n" \
                         "*                    *\n" \
                         "*                    *\n" \
                         "*****         **     *\n" \
                         "*   *         **     *\n" \
                         "*   ************     *\n" \
                         "*                    *\n" \
                         "*                    *\n" \
                         "**********************\n"

vars['corridor'] = "......................\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     "......................\n"


##################################################################################

height['corridor_new_texture'] =  "9999999999999999999999\n" \
                                  "9               5    9\n" \
                                  "9               5    9\n" \
                                  "9    555555555555    9\n" \
                                  "9    5               9\n" \
                                  "9    5          555559\n" \
                                  "9    5          5    9\n" \
                                  "9         5555555    9\n" \
                                  "9                    9\n" \
                                  "9         555555555559\n" \
                                  "9       55555555555559\n" \
                                  "9       5            9\n" \
                                  "9       5   5555555559\n" \
                                  "9       5   5        9\n" \
                                  "9       5   5        9\n" \
                                  "9           5  5555559\n" \
                                  "9    55        5555559\n" \
                                  "9    555555555555    9\n" \
                                  "9    555555555555    9\n" \
                                  "9                    9\n" \
                                  "9                    9\n" \
                                  "9999999999999999999999\n"

mazes['corridor_new_texture'] =  "**********************\n" \
                                 "*               *    *\n" \
                                 "*               *    *\n" \
                                 "*    ************    *\n" \
                                 "*    *               *\n" \
                                 "*    *          ******\n" \
                                 "*    *          *    *\n" \
                                 "*         *******    *\n" \
                                 "*                    *\n" \
                                 "*         ************\n" \
                                 "*       **************\n" \
                                 "*       *            *\n" \
                                 "*       *   **********\n" \
                                 "*   0   *   *       G*\n" \
                                 "*       *   *        *\n" \
                                 "*           *  *******\n" \
                                 "*    **        *******\n" \
                                 "*    ************    *\n" \
                                 "*    ************    *\n" \
                                 "*                    *\n" \
                                 "*                    *\n" \
                                 "**********************\n"

walls['corridor_new_texture'] =  "**********************\n" \
                                 "*               *    *\n" \
                                 "*               *    *\n" \
                                 "*    ************    *\n" \
                                 "*    *               ^\n" \
                                 "*    *          ^^^^^^\n" \
                                 "*    *          ^    ^\n" \
                                 "*         ^^^^^^^    ^\n" \
                                 "*                    ^\n" \
                                 "*         ^^^^^^^^^^^^\n" \
                                 "*       **************\n" \
                                 "*       *            *\n" \
                                 "*       *   **********\n" \
                                 "*       *   *        *\n" \
                                 "*       *   *        *\n" \
                                 "*           *  *******\n" \
                                 "*    ^*        *^^^^^^\n" \
                                 "*    ^**********^    ^\n" \
                                 "^    ^^^^^^^^^^^^    ^\n" \
                                 "^                    ^\n" \
                                 "^                    ^\n" \
                                 "^^^^^^^^^^^^^^^^^^^^^^\n"

vars['corridor_new_texture'] = "......................\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAA.\n" \
                             "......................\n"

############################################################################################


height['violation1'] =  "9999999999999999999999\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9           5        9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9999999999999999999999\n"

mazes['violation1'] =  "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*           *        *\n" \
                     "*     1     *        *\n" \
                     "*           *        *\n" \
                     "*           *        *\n" \
                     "*0          *        G\n" \
                     "*           *        *\n" \
                     "*           *        *\n" \
                     "*     2     *        *\n" \
                     "*           *        *\n" \
                     "*           *        *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "**********************\n"

walls['violation1'] =  "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*           *        *\n" \
                     "*           *        *\n" \
                     "*           *        *\n" \
                     "*           *        *\n" \
                     "*           *         \n" \
                     "*           *        *\n" \
                     "*           !        *\n" \
                     "*           !        *\n" \
                     "*           !        *\n" \
                     "*           *        *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "**********************\n"

vars['violation1'] =   "......................\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     "......................\n"


############################################################################################
height['violation2'] = height['dynamics']
mazes['violation2'] = mazes['dynamics']
walls['violation2'] = walls['dynamics']
vars['violation2'] = vars['dynamics']

############################################################################################
height['colorchange'] = height['dynamics']
mazes['colorchange'] = mazes['dynamics']
walls['colorchange'] = walls['dynamics']
vars['colorchange'] = vars['dynamics']

############################################################################################
height['colorchange_collision'] = height['dynamics']
walls['colorchange_collision'] = walls['dynamics']
vars['colorchange_collision'] = vars['dynamics']
mazes['colorchange_collision'] =  \
                     "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*         2          *\n" \
                     "*        403         *\n" \
                     "*         1          G\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "**********************\n"
############################################################################################

height['massdiff'] =  "9999999999999999999999\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9                    9\n" \
                      "9999999999999999999999\n"

mazes['massdiff'] =  "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*      1         2   *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*     2              *\n" \
                     "*             1      *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*        0           G\n" \
                     "*                    *\n" \
                     "*              2     *\n" \
                     "*                    *\n" \
                     "*    2               *\n" \
                     "*       1            *\n" \
                     "*                    *\n" \
                     "*          2         *\n" \
                     "*                    *\n" \
                     "*     1              *\n" \
                     "*                    *\n" \
                     "**********************\n"

walls['massdiff'] =  "**********************\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "*                    *\n" \
                     "**********************\n"

vars['massdiff'] =   "......................\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     ".AAAAAAAAAAAAAAAAAAAA.\n" \
                     "......................\n"

############################################################################################
height['homecage'] =        "999999999999999999999\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "999999999999999999999\n"

mazes['homecage'] =          "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*         0        G*\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

walls['homecage'] =          "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

vars['homecage'] =           ".....................\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".....................\n"


height['novel_objects'] =   "999999999999999999999\n" \
                            "9                   9\n" \
                            "999999999999999999999\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "999999999999999999999\n"

mazes['novel_objects'] =    "*********************\n" \
                             "* 1 2 3 4           *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*         0        G*\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

walls['novel_objects'] =     "*********************\n" \
                             "*                   *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

vars['novel_objects'] =      ".....................\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".....................\n"


height['object_example'] =  "999999999999999999999\n" \
                            "9                   9\n" \
                            "999999999999999999999\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "999999999999999999999\n"

mazes['object_example'] =    "*********************\n" \
                             "* 1 2 3 4           *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                  G*\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*         0         *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

walls['object_example'] =    "*********************\n" \
                             "*                   *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

vars['object_example'] =     ".....................\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".....................\n"




height['object_example2'] = "999999999999999999999\n" \
                            "9                   9\n" \
                            "999999999999999999999\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "999999999999999999999\n"

mazes['object_example2'] =   "*********************\n" \
                             "* 1 2 3 4           *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                  G*\n" \
                             "*                   *\n" \
                             "*         0         *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

walls['object_example2'] =   "*********************\n" \
                             "*                   *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

vars['object_example2'] =    ".....................\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".....................\n"



height['object_example3'] = "999999999999999999999\n" \
                            "9                   9\n" \
                            "999999999999999999999\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "999999999999999999999\n"

mazes['object_example3'] =   "*********************\n" \
                             "* 1 2 3 4           *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*         0         *\n" \
                             "*                   *\n" \
                             "*                  G*\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

walls['object_example3'] =   "*********************\n" \
                             "*                   *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

vars['object_example3'] =    ".....................\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".....................\n"


height['object_example4'] = "999999999999999999999\n" \
                            "9                   9\n" \
                            "999999999999999999999\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "9                   9\n" \
                            "999999999999999999999\n"

mazes['object_example4'] =   "*********************\n" \
                             "* 1 2 3 4           *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                  G*\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*    0              *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

walls['object_example4'] =   "*********************\n" \
                             "*                   *\n" \
                             "*********************\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*                   *\n" \
                             "*********************\n"

vars['object_example4'] =    ".....................\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAA.\n" \
                             ".....................\n"



height['sparse_goal'] =     "99999999999999999999999\n" \
                            "99                   99\n" \
                            "99999999999999999999999\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99                   99\n" \
                            "99999999999999999999999\n" \
                            "99999999999999999999999\n"

mazes['sparse_goal'] =       "***********************\n" \
                             "** 1 2 3 4           **\n" \
                             "***********************\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**         0         **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**              G    **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "***********************\n" \
                             "***********************\n"

walls['sparse_goal'] =       "***********************\n" \
                             "**                   **\n" \
                             "**g*****************g**\n" \
                             "*g                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   g*\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "**                   **\n" \
                             "*g                   **\n" \
                             "****************g******\n" \
                             "***********************\n"

vars['sparse_goal'] =        ".......................\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".......................\n"



height['openfield'] = \
                             "99999999999999999999999999999999999999999\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "9                                       9\n" \
                             "99999999999999999999999999999999999999999\n" \

mazes['openfield'] = \
                             "*****************************************\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*     0                            G    *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*****************************************\n" \

walls['openfield'] = \
                             "*****************************************\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*                                       *\n" \
                             "*****************************************\n" \

vars['openfield'] = \
                             "*****************************************\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".........................................\n" \



height['distal'] = \
                             "99999999999999999999999999999999999999999999\n" \
                             "9      9                                   9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                            8             9\n" \
                             "9     44444444444444444444444444444444     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              49    9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9 9   4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4   9 9\n" \
                             "99    4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     44444444444444444444444444444444     9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                     9                    9\n" \
                             "9                                          9\n" \
                             "99999999999999999999999999999999999999999999\n" \

mazes['distal'] = \
                             "********************************************\n" \
                             "*      *                                   *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*      1234                  *             *\n" \
                             "*     ********************************     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              **    *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "* *   *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *   0                        G *   * *\n" \
                             "**    *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     ********************************     *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                     *                    *\n" \
                             "*                                          *\n" \
                             "********************************************\n" \

walls['distal'] = \
                             "********************************************\n" \
                             "*      *                                   *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                            *             *\n" \
                             "*     ********************************     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              **    *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "* *   *                              *     *\n" \
                             "*     g                              *     *\n" \
                             "*     *                              *   * *\n" \
                             "**    *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     ********************************     *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                     *                    *\n" \
                             "*                                          *\n" \
                             "********************************************\n" \

vars['distal'] = \
                             "********************************************\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             "............................................\n" \


height['distal_c1'] = \
                             "99999999999999999999999999999999999999999999\n" \
                             "9      9                                   9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                            8             9\n" \
                             "9     44444444444444444444444444444444     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              49    9\n" \
                             "9     4                    6         4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9 9   4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4   9 9\n" \
                             "99    4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     44444444444444444444444444444444     9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                     9                    9\n" \
                             "9                                          9\n" \
                             "99999999999999999999999999999999999999999999\n" \

mazes['distal_c1'] = \
                             "********************************************\n" \
                             "*      *                                   *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*      1234                  *             *\n" \
                             "*     ********************************     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              **    *\n" \
                             "*     *                    *         *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "* *   *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *   0                        G *   * *\n" \
                             "**    *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     ********************************     *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                     *                    *\n" \
                             "*                                          *\n" \
                             "********************************************\n" \

walls['distal_c1'] = \
                             "********************************************\n" \
                             "*      *                                   *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                            *             *\n" \
                             "*     ********************************     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              **    *\n" \
                             "*     *                    g         *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "* *   *                              *     *\n" \
                             "*     g                              *     *\n" \
                             "*     *                              *   * *\n" \
                             "**    *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     ********************************     *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                     *                    *\n" \
                             "*                                          *\n" \
                             "********************************************\n" \

vars['distal_c1'] = \
                             "********************************************\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             "............................................\n" \

height['distal_c2'] = \
                             "99999999999999999999999999999999999999999999\n" \
                             "9      9                                   9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                            8             9\n" \
                             "9     44444444444444444444444444444444     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              49    9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9 9   4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4   9 9\n" \
                             "99    4                6             4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     4                              4     9\n" \
                             "9     44444444444444444444444444444444     9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                                          9\n" \
                             "9                     9                    9\n" \
                             "9                                          9\n" \
                             "99999999999999999999999999999999999999999999\n" \

mazes['distal_c2'] = \
                             "********************************************\n" \
                             "*      *                                   *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*      1234                  *             *\n" \
                             "*     ********************************     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              **    *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "* *   *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *   0                        G *   * *\n" \
                             "**    *                *             *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     ********************************     *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                     *                    *\n" \
                             "*                                          *\n" \
                             "********************************************\n" \

walls['distal_c2'] = \
                             "********************************************\n" \
                             "*      *                                   *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                            *             *\n" \
                             "*     ********************************     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              **    *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "* *   *                              *     *\n" \
                             "*     g                              *     *\n" \
                             "*     *                              *   * *\n" \
                             "**    *                g             *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     *                              *     *\n" \
                             "*     ********************************     *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                                          *\n" \
                             "*                     *                    *\n" \
                             "*                                          *\n" \
                             "********************************************\n" \

vars['distal_c2'] = \
                             "********************************************\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                             "............................................\n" \




mazes['labyrinth'] =       \
                            "***************************************************\n" \
                            "*                   *     ***     ***     ***     *\n" \
                            "*                   *** ******* ******* ******* ***\n" \
                            "*                   ***         *******         ***\n" \
                            "*                   *** *** *** ******* *** *** ***\n" \
                            "*********************     * *     ***     * *     *\n" \
                            "*                   ******* *************** *******\n" \
                            "*                   *******                 *******\n" \
                            "*                   ******* ******* ******* *******\n" \
                            "*                   *     * *     * *     * *     *\n" \
                            "*                   *** *** *** *** *** *** *** ***\n" \
                            "*                   ***         *** ***         ***\n" \
                            "*                   *** ******* *** *** ******* ***\n" \
                            "*                   *     ***     * *     ***     *\n" \
                            "*                   *************** ***************\n" \
                            "*  G     0                          ***************\n" \
                            "*                   *************** ***************\n" \
                            "*                   *     ***     * *     ***     *\n" \
                            "*                   *** ******* *** *** ******* ***\n" \
                            "*                   ***         *** ***         ***\n" \
                            "*                   *** *** *** *** *** *** *** ***\n" \
                            "*                   *     * *     * *     * *     *\n" \
                            "*                   ******* ******* ******* *******\n" \
                            "*                   *******                 *******\n" \
                            "*                   ******* *************** *******\n" \
                            "*********************     * *     ***     * *     *\n" \
                            "*                   *** *** *** ******* *** *** ***\n" \
                            "*                   ***         *******         ***\n" \
                            "*                   *** ******* ******* ******* ***\n" \
                            "*                   *     ***     ***     ***     *\n" \
                            "***************************************************\n" \

height['labyrinth'] =       \
                            "999999999999999999999999999999999999999999999999999\n" \
                            "9                   9     999     999     999     9\n" \
                            "9                   999 9999999 9999999 9999999 999\n" \
                            "9                   999         9999999         999\n" \
                            "9                   999 999 999 9999999 999 999 999\n" \
                            "999999999999999999999     9 9     999     9 9     9\n" \
                            "9                   9999999 999999999999999 9999999\n" \
                            "9                   9999999                 9999999\n" \
                            "9                   9999999 9999999 9999999 9999999\n" \
                            "9                   9     9 9     9 9     9 9     9\n" \
                            "9                   999 999 999 999 999 999 999 999\n" \
                            "9                   999         999 999         999\n" \
                            "9                   999 9999999 999 999 9999999 999\n" \
                            "9                   9     999     9 9     999     9\n" \
                            "9                   999999999999999 999999999999999\n" \
                            "9                                   999999999999999\n" \
                            "9                   999999999999999 999999999999999\n" \
                            "9                   9     999     9 9     999     9\n" \
                            "9                   999 9999999 999 999 9999999 999\n" \
                            "9                   999         999 999         999\n" \
                            "9                   999 999 999 999 999 999 999 999\n" \
                            "9                   9     9 9     9 9     9 9     9\n" \
                            "9                   9999999 9999999 9999999 9999999\n" \
                            "9                   9999999                 9999999\n" \
                            "9                   9999999 999999999999999 9999999\n" \
                            "999999999999999999999     9 9     999     9 9     9\n" \
                            "9                   999 999 999 9999999 999 999 999\n" \
                            "9                   999         9999999         999\n" \
                            "9                   999 9999999 9999999 9999999 999\n" \
                            "9                   9     999     999     999     9\n" \
                            "999999999999999999999999999999999999999999999999999\n" \

walls['labyrinth'] =       \
                            "***************************************************\n" \
                            "*                   *     ***     ***     ***     *\n" \
                            "*                   *** ******* ******* ******* ***\n" \
                            "*                   ***         *******         ***\n" \
                            "*                   *** *** *** ******* *** *** ***\n" \
                            "*********************     * *     ***     * *     *\n" \
                            "*                   ******* *************** *******\n" \
                            "*                   *******                 *******\n" \
                            "*                   ******* ******* ******* *******\n" \
                            "*                   *     * *     * *     * *     *\n" \
                            "*                   *** *** *** *** *** *** *** ***\n" \
                            "*                   ***         *** ***         ***\n" \
                            "*                   *** ******* *** *** ******* ***\n" \
                            "*                   *     ***     * *     ***     *\n" \
                            "*                   *************** ***************\n" \
                            "*                                   ***************\n" \
                            "*                   *************** ***************\n" \
                            "*                   *     ***     * *     ***     *\n" \
                            "*                   *** ******* *** *** ******* ***\n" \
                            "*                   ***         *** ***         ***\n" \
                            "*                   *** *** *** *** *** *** *** ***\n" \
                            "*                   *     * *     * *     * *     *\n" \
                            "*                   ******* ******* ******* *******\n" \
                            "*                   *******                 *******\n" \
                            "*                   ******* *************** *******\n" \
                            "*********************     * *     ***     * *     *\n" \
                            "*                   *** *** *** ******* *** *** ***\n" \
                            "*                   ***         *******         ***\n" \
                            "*                   *** ******* ******* ******* ***\n" \
                            "*                   *     ***     ***     ***     *\n" \
                            "***************************************************\n" \

vars['labyrinth'] =       \
                            "...................................................\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            "...................................................\n" \



mazes['labyrinth_fast'] =       \
                            "*****************************************\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *** ******* ******* ******* ***\n" \
                            "*         ***         *     *         ***\n" \
                            "*         *** *** *** ******* *** *** ***\n" \
                            "***********     * *     ***     * *     *\n" \
                            "*         ******* *************** *******\n" \
                            "*         *******                 *******\n" \
                            "*         ******* ******* ******* *******\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *** *** *** *** *** *** *** ***\n" \
                            "*         ***         *** ***         ***\n" \
                            "*         *** ******* *** *** ******* ***\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *************** ***************\n" \
                            "*G   0                    ***************\n" \
                            "*         *************** ***************\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *** ******* *** *** ******* ***\n" \
                            "*         ***         *** ***         ***\n" \
                            "*         *** *** *** *** *** *** *** ***\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         ******* ******* ******* *******\n" \
                            "*         *******                 *******\n" \
                            "*         ******* *************** *******\n" \
                            "***********     * *     ***     * *     *\n" \
                            "*         *** *** *** ******* *** *** ***\n" \
                            "*         ***         *     *         ***\n" \
                            "*         *** ******* ******* ******* ***\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*****************************************\n" \

height['labyrinth_fast'] =       \
                            "99999999999999999999999999999999999999999\n" \
                            "9         9     9 9     9 9     9 9     9\n" \
                            "9         999 9999999 9999999 9999999 999\n" \
                            "9         999         9     9         999\n" \
                            "9         999 999 999 9999999 999 999 999\n" \
                            "99999999999     9 9     999     9 9     9\n" \
                            "9         9999999 999999999999999 9999999\n" \
                            "9         9999999                 9999999\n" \
                            "9         9999999 9999999 9999999 9999999\n" \
                            "9         9     9 9     9 9     9 9     9\n" \
                            "9         999 999 999 999 999 999 999 999\n" \
                            "9         999         999 999         999\n" \
                            "9         999 9999999 999 999 9999999 999\n" \
                            "9         9     9 9     9 9     9 9     9\n" \
                            "9         999999999999999 999999999999999\n" \
                            "9                         999999999999999\n" \
                            "9         999999999999999 999999999999999\n" \
                            "9         9     9 9     9 9     9 9     9\n" \
                            "9         999 9999999 999 999 9999999 999\n" \
                            "9         999         999 999         999\n" \
                            "9         999 999 999 999 999 999 999 999\n" \
                            "9         9     9 9     9 9     9 9     9\n" \
                            "9         9999999 9999999 9999999 9999999\n" \
                            "9         9999999                 9999999\n" \
                            "9         9999999 999999999999999 9999999\n" \
                            "99999999999     9 9     999     9 9     9\n" \
                            "9         999 999 999 9999999 999 999 999\n" \
                            "9         999         9     9         999\n" \
                            "9         999 9999999 9999999 9999999 999\n" \
                            "9         9     9 9     9 9     9 9     9\n" \
                            "99999999999999999999999999999999999999999\n" \

walls['labyrinth_fast'] =       \
                            "*****************************************\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *** ******* ******* ******* ***\n" \
                            "*         ***         *     *         ***\n" \
                            "*         *** *** *** ******* *** *** ***\n" \
                            "***********     * *     ***     * *     *\n" \
                            "*         ******* *************** *******\n" \
                            "*         *******                 *******\n" \
                            "*         ******* ******* ******* *******\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *** *** *** *** *** *** *** ***\n" \
                            "*         ***         *** ***         ***\n" \
                            "*         *** ******* *** *** ******* ***\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *************** ***************\n" \
                            "*                         ***************\n" \
                            "*         *************** ***************\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         *** ******* *** *** ******* ***\n" \
                            "*         ***         *** ***         ***\n" \
                            "*         *** *** *** *** *** *** *** ***\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*         ******* ******* ******* *******\n" \
                            "*         *******                 *******\n" \
                            "*         ******* *************** *******\n" \
                            "***********     * *     ***     * *     *\n" \
                            "*         *** *** *** ******* *** *** ***\n" \
                            "*         ***         *     *         ***\n" \
                            "*         *** ******* ******* ******* ***\n" \
                            "*         *     * *     * *     * *     *\n" \
                            "*****************************************\n" \

vars['labyrinth_fast'] =       \
                            ".........................................\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.\n" \
                            ".........................................\n" \


def get_custom_maze(id):
  """Returns all layers defining a custom maze."""
  return mazes[id], vars[id], height[id], walls[id]
